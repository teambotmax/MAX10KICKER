# -*- coding: utf-8 -*-

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin

class Channel(object):
    isLogin = False
    channelId     = None
    channelResult = None

    def __init__(self, client, channelId, showSuccess=True):
        self.client = client
        self.channelId = channelId
        self.showSuccess = showSuccess
        self.__loginChannel()

    def __logChannel(self, text):
        self.client.log('[%s] : Success login to %s' % (self.client.profile.displayName, text))

    def __loginChannel(self):
        self.isLogin = True
        self.channelResult  = self.approveChannelAndIssueChannelToken(self.channelId)
        self.__createChannelSession()

    @loggedIn
    def getChannelResult(self):
        return self.channelResult

    def __createChannelSession(self):
        channelInfo = self.getChannelInfo(self.channelId)
        if self.showSuccess:
            self.__logChannel(channelInfo.name)

    @loggedIn
    def approveChannelAndIssueChannelToken(self, channelId):
        return self.client.approveChannelAndIssueChannelToken(channelId)

    @loggedIn
    def updateProfile(self, profileObject):
        return self.talk.updateProfile(0, profileObject)

    @loggedIn
    def updateSettings(self, settingObject):
        return self.talk.updateSettings(0, settingObject)

    @loggedIn
    def updateProfileAttribute(self, attrId, value):
        return self.talk.updateProfileAttribute(0, attrId, value)


    @loggedIn
    def sendFooter(self, to, text, link, icon, footer):
        contentMetadata = {'AGENT_LINK': link, 'AGENT_ICON': icon, 'AGENT_NAME': footer}
        return self.sendMessage(to, text, contentMetadata)

    @loggedIn
    def cloneContactProfile(self, mid):
        contact = self.getContact(mid)
        profile = self.profile
        profile.displayName = contact.displayName
        profile.statusMessage = contact.statusMessage
        profile.pictureStatus = contact.pictureStatus
        if self.getProfileCoverId(mid) is not None:
            self.updateProfileCoverById(self.getProfileCoverId(mid))
        self.updateProfileAttribute(8, profile.pictureStatus)
        return self.updateProfile(profile)

    """Group"""

    @loggedIn
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @loggedIn
    def cloneContactProfile(self, mid):
        contact = self.getContact(mid)
        profile = self.profile
        profile.displayName = contact.displayName
        profile.statusMessage = contact.statusMessage
        profile.pictureStatus = contact.pictureStatus
        if self.getProfileCoverId(mid) is not None:
            self.updateProfileCoverById(self.getProfileCoverId(mid))
        self.updateProfileAttribute(8, profile.pictureStatus)
        return self.updateProfile(profile)

    """Group"""

    @loggedIn
    def issueChannelToken(self, channelId):
        return self.client.issueChannelToken(channelId)

    @loggedIn
    def getChannelInfo(self, channelId, locale='EN'):
        return self.client.getChannelInfo(channelId, locale)

    @loggedIn
    def revokeChannel(self, channelId):
        return self.client.revokeChannel(channelId)