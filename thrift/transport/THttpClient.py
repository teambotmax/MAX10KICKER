#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

from io import BytesIO
import os
import socket
import sys
import warnings
import base64
import time

from six.moves import urllib
from six.moves import http_client

from .TTransport import TTransportBase
import six


class THttpClient(TTransportBase):
    """Http implementation of TTransport base."""

    def __init__(self, uri_or_host, speedThrift=False, port=None, path=None):
        """THttpClient supports two different types constructor parameters.

        THttpClient(host, port, path) - deprecated
        THttpClient(uri)

        Only the second supports https.
        """
        if port is not None:
            warnings.warn(
                "Please use the THttpClient('http://host:port/path') syntax",
                DeprecationWarning,
                stacklevel=2)
            self.host = uri_or_host
            self.port = port
            assert path
            self.path = path
            self.scheme = 'http'
        else:
            parsed = urllib.parse.urlparse(uri_or_host)
            self.scheme = parsed.scheme
            assert self.scheme in ('http', 'https')
            if self.scheme == 'http':
                self.port = parsed.port or http_client.HTTP_PORT
            elif self.scheme == 'https':
                self.port = parsed.port or http_client.HTTPS_PORT
            self.host = parsed.hostname
            self.path = parsed.path
            if parsed.query:
                self.path += '?%s' % parsed.query
        proxy = None
        self.realhost = self.realport = self.proxy_auth = None
        self.__wbuf = BytesIO()
        self.__http = None
        self.__http_response = None
        self.__timeout = None
        self.__custom_headers = None
        self.__speedThrift = speedThrift        
        self.__time = time.time()
        self.__loop = 0

    @staticmethod
    def basic_proxy_auth_header(proxy):
        if proxy is None or not proxy.username:
            return None
        ap = "%s:%s" % (urllib.parse.unquote(proxy.username),
                        urllib.parse.unquote(proxy.password))
        cr = base64.b64encode(ap).strip()
        return "Basic " + cr

    def using_proxy(self):
        return self.realhost is not None

    def open(self):
        if self.scheme == 'http':
            self.__http = http_client.HTTPConnection(self.host, self.port)
        elif self.scheme == 'https':
            self.__http = http_client.HTTPSConnection(self.host, self.port)

    def close(self):
        self.__http.close()
        self.__http = None
        self.__http_response = None

    def isOpen(self):
        return self.__http is not None

    def setTimeout(self, ms):
        if not hasattr(socket, 'getdefaulttimeout'):
            raise NotImplementedError

        if ms is None:
            self.__timeout = None
        else:
            self.__timeout = ms / 1000.0

    def setCustomHeaders(self, headers):
        self.__custom_headers = headers

    def read(self, sz):
        return self.__http_response.read(sz)

    def write(self, buf):
        self.__wbuf.write(buf)

    def __withTimeout(f):
        def _f(*args, **kwargs):
            orig_timeout = socket.getdefaulttimeout()
            socket.setdefaulttimeout(args[0].__timeout)
            try:
                result = f(*args, **kwargs)
            finally:
                socket.setdefaulttimeout(orig_timeout)
            return result
        return _f

    def flush(self):
        if self.__loop <= 2:
            if self.isOpen(): self.close()
            self.open(); self.__loop += 1
        elif time.time() - self.__time > 120:
            self.close(); self.open(); self.__time = time.time()

        # Pull data out of buffer
        data = self.__wbuf.getvalue()
        self.__wbuf = BytesIO()

        self.__http.putrequest('POST', self.path)

        # Write headers
        self.__http.putheader('Host', self.host)
        self.__http.putheader('Content-Type', 'application/x-thrift')
        self.__http.putheader('Content-Length', str(len(data)))
        if self.__custom_headers:
            for key, val in six.iteritems(self.__custom_headers):
                self.__http.putheader(key, val)

        self.__http.endheaders()

        # Write payload
        self.__http.send(data)

        # Get reply to flush the request
        self.__http_response = self.__http.getresponse()
        self.code = self.__http_response.status
        self.message = self.__http_response.reason
        self.headers = self.__http_response.msg
