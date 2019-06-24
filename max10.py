#=====================================================================
# ＳＥＬＦＢＯＴＢＹＭＡＸ
#=====================================================================
import MAXPY
from MAXPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#=====================================================================
# ＳＥＬＦＢＯＴＢＹＭＡＸ
#=====================================================================
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Admin Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
aditmadzs = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 1 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k1 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 2 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k2 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 3 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k3 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 4 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k4 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 5 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k5 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 6 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k6 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 7 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k7 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 8 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k8 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 9 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k9 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Kicker 10 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
k10 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Ghost1 Login 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
g1 = LINE("")
print ("-▬▬▬▬▬▬▬▬▬▬▬▬▬「 Login succeeded. 」▬▬▬▬▬▬▬▬▬▬▬▬▬-")
#=====================================================================
oepoll = OEPoll(aditmadzs)
call = aditmadzs
aditmadzsProfile = aditmadzs.getProfile()
creator = ["ufe4133018ba612fd5e32ad7db17ba54e"]
owner = ["u1794f175bac96f66461ed36ba70808cd"]
admin = ["u1794f175bac96f66461ed36ba70808cd"]
staff = ["ufe4133018ba612fd5e32ad7db17ba54e"]
mid = aditmadzs.getProfile().mid
Amid = k1.getProfile().mid
Bmid = k2.getProfile().mid
Cmid = k3.getProfile().mid
Dmid = k4.getProfile().mid
Emid = k5.getProfile().mid
Fmid = k6.getProfile().mid
Gmid = k7.getProfile().mid
Hmid = k8.getProfile().mid
Imid = k9.getProfile().mid
Jmid = k10.getProfile().mid   
g1MID = g1.getProfile().mid
KAC = [aditmadzs,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]
ABC = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]
KICKER = [g1]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID]
Aditmadzs = admin + staff
#=====================================================================
pendings = []
zxcv = mid
protectqr = []
protectkick = []
protectkick1 = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
#=====================================================================
welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []
#=====================================================================
responsename1 = k1.getProfile().displayName
responsename2 = k2.getProfile().displayName
responsename3 = k3.getProfile().displayName
responsename4 = k4.getProfile().displayName
responsename5 = k5.getProfile().displayName
responsename6 = k6.getProfile().displayName
responsename7 = k7.getProfile().displayName
responsename8 = k8.getProfile().displayName
responsename9 = k9.getProfile().displayName
responsename10 = k10.getProfile().displayName
#=====================================================================
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

aditProfile = aditmadzs.getProfile()
myProfile["displayName"] = aditProfile.displayName
myProfile["statusMessage"] = aditProfile.statusMessage
myProfile["pictureStatus"] = aditProfile.pictureStatus

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    
with open('protectqr.json', 'r') as fp:
    protectqr = json.load(fp)
with open('protectantijs.json', 'r') as fp:
    protectantijs = json.load(fp)
with open('ghost.json', 'r') as fp:
    ghost = json.load(fp)

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
          
def searchRecentMessages(to,id):
    for a in client.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None
  
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k1.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k2.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention3(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k3.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention4(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k4.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention5(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k5.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention6(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k6.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention7(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k7.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMention8(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k8.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention9(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k9.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention10(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k10.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╰──「 {} 」".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n╰──「 Success 」"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╰──「 {} 」".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n╰──「 Success 」"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╰──「 {} 」".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n╰──「 Success 」"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╰──「 {} 」".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n╰──「 Success 」"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = aditmadzs.getAllContactIds()
        gid = aditmadzs.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+"\n◐ Group : "+str(len(gid))+"\n◐ Teman : "+str(len(teman))+"\n◐ Expired : In "+hari+"\n◐ Version : 2019\n◐ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n◐ Runtime : \n • "+bot
        aditmadzs.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭────────────────────" + "\n" + \
                  "│    ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰────────────────────" + "\n" + \
                  "╭────────────────────" + "\n" + \
                  "│➣                ＨＥＬＰ" + "\n" + \
                  "┝────────────────────" + "\n" + \
                  "│➣ " + key + "Help\n" + \
                  "│➣ " + key + "Help bot\n" + \
                  "│➣ " + key + "Help group\n" + \
                  "│➣ " + key + "Help media\n" + \
                  "│➣ " + key + "Help setting\n" + \
                  "│➣ " + key + "Help protect\n" + \
                  "│➣ " + key + "Help admin\n" + \
                  "│➣ " + key + "Me\n" + \
                  "│➣ " + key + "Mymid\n" + \
				  "│➣ " + key + "Leave:「Namagrup」\n" + \
                  "│➣ " + key + "Spamtag「jumlahnya」+「@」\n" + \
                  "│➣ " + key + "Spamcallto「jumlahnya」+「@」\n" + \
                  "│➣ " + key + "Spamcall\n" + \
                  "│➣ " + key + "Spaminvite\n" + \
                  "│➣ " + key + "Spamchat「on/off」+「text」\n" + \
                  "│➣ " + key + "Getcover 「@」\n" + \
                  "│➣ " + key + "Mid「@」\n" + \
                  "│➣ " + key + "Info 「@」\n" + \
                  "│➣ " + key + "Kick 「@」\n" + \
                  "│➣ " + key + "Vk 「@」\n" + \
                  "│➣ " + key + "Bk 「@」\n" + \
                  "│➣ " + key + "Nk 「@」\n" + \
                  "│➣ " + key + "Mybot\n" + \
                  "│➣ " + key + "In\n" + \
                  "│➣ " + key + "Out\n" + \
                  "│➣ " + key + "Status\n" + \
                  "│➣ " + key + "About\n" + \
                  "│➣ " + key + "Restart\n" + \
                  "│➣ " + key + "Runtime\n" + \
                  "│➣ " + key + "Creator\n" + \
                  "│➣ " + key + "Respon\n" + \
                  "│➣ " + key + "Speed\n" + \
                  "│➣ " + key + "Speedbot\n" + \
                  "│➣ " + key + "Pendinglist\n" + \
                  "│➣ " + key + "All mid\n" + \
                  "│➣ " + key + "Tag\n" + \
                  "┝────────────────────" + "\n" + \
                  "│    ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "┝────────────────────" + "\n" + \
                  "│http://line.me/ti/p/%40jnx0914l" + "\n" + \
                  "╰────────────────────"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────" + "\n" + \
                  "╭──────────────────" + "\n" + \
                  "│➣        ＨＥＬＰ ＢＯＴ" + "\n" + \
                  "┝──────────────────" + "\n" + \
				  "│➣ " + key + "Self「on/off」\n" + \
                  "│➣ " + key + "Set autoadd:「Text」\n" + \
                  "│➣ " + key + "Set autoblock:「Text」\n" + \
                  "│➣ " + key + "Set autojoin:「Text」\n" + \
                  "│➣ " + key + "Set member:「Number」\n" + \
                  "│➣ " + key + "Set respon:「Text」\n" + \
                  "│➣ " + key + "Set welcome:「Text」\n" + \
                  "│➣ " + key + "Set leave:「Text」\n" + \
                  "│➣ " + key + "Name:「Nama」\n" + \
                  "│➣ " + key + "1-10name:「Nama」\n" + \
                  "│➣ " + key + "1-10up「Kirim fotonya」\n" + \
				  "│➣ " + key + "Spamtag:「jumlahnya」\n" + \
                  "│➣ " + key + "Spamtag「@」\n" + \
                  "│➣ " + key + "Spamcall:「jumlahnya」\n" + \
                  "│➣ " + key + "Spamcall\n" + \
				  "│➣ " + key + "Updatefoto\n" + \
                  "│➣ " + key + "Updategrup\n" + \
                  "│➣ " + key + "Upbot\n" + \
                  "┝──────────────────" + "\n" + \
                  "│➣             Blacklist" + "\n" + \
                  "┝──────────────────" + "\n" + \
                  "│➣ " + key + "Inv\n" + \
                  "│➣ " + key + "Respon\n" + \
                  "│➣ " + key + "Name\n" + \
                  "│➣ " + key + "Bc\n" + \
                  "│➣ " + key + "Cb\n" + \
                  "│➣ " + key + "Ban:on\n" + \
                  "│➣ " + key + "Unban:on\n" + \
                  "│➣ " + key + "Ban「@」\n" + \
                  "│➣ " + key + "Unban「@」\n" + \
                  "│➣ " + key + "Talkban「@」\n" + \
                  "│➣ " + key + "Untalkban「@」\n" + \
                  "│➣ " + key + "Talkban:on\n" + \
                  "│➣ " + key + "Untalkban:on\n" + \
                  "│➣ " + key + "Banlist\n" + \
                  "│➣ " + key + "Talkbanlist\n" + \
                  "│➣ " + key + "Refresh\n" + \
                  "┝──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────"
    return helpMessage1

def helpgroup():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╭──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────" + "\n" + \
                  "╭──────────────────" + "\n" + \
                  "│➣     ＨＥＬＰ ＧＲＯＵＰ" + "\n" + \
                  "┝──────────────────" + "\n" + \
                  "│➣ " + key + "Mention\n" + \
                  "│➣ " + key + "Groupbc:「Text」\n" + \
                  "│➣ " + key + "Friendbc:「Text」\n" + \
                  "│➣ " + key + "Myname\n" + \
                  "│➣ " + key + "Mybio\n" + \
                  "│➣ " + key + "Mypicture\n" + \
                  "│➣ " + key + "Myvideoprofile\n" + \
                  "│➣ " + key + "Mycover\n" + \
                  "│➣ " + key + "Mycover url\n" + \
                  "│➣ " + key + "Ginfo\n" + \
                  "│➣ " + key + "Open\n" + \
                  "│➣ " + key + "Close\n" + \
                  "│➣ " + key + "Url grup\n" + \
                  "│➣ " + key + "Reject\n" + \
                  "│➣ " + key + "Gruplist\n" + \
                  "│➣ " + key + "Infogrup「angka」\n" + \
                  "│➣ " + key + "Infomem「angka」\n" + \
                  "│➣ " + key + "Lurking「on/off」\n" + \
                  "│➣ " + key + "Lurkers\n" + \
                  "│➣ " + key + "Sider「on/off」\n" + \
                  "│➣ " + key + "Setkey「New Key」\n" + \
                  "│➣ " + key + "Mykey\n" + \
                  "│➣ " + key + "Resetkey\n" + \
                  "┝──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────"
    return helpMessage2
    
def helpmedia():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╭──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────" + "\n" + \
                  "╭──────────────────" + "\n" + \
                  "│➣    ＨＥＬＰ ＭＥＤＩＡ" + "\n" + \
                  "┝──────────────────" + "\n" + \
                  "│➣ " + key + "Musik:「Judul Lagu」\n" + \
                  "│➣ " + key + "Musik2:「Judul Lagu」\n" + \
                  "│➣ " + key + "Playlist「Nama Penyanyi」\n" + \
                  "│➣ " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "│➣ " + key + "Ytmp4:「Judul Video\n" + \
                  "│➣ " + key + "Meme@Nama@Teks1@Teks2\n" + \
                  "│➣ " + key + "1cak\n" + \
                  "│➣ " + key + "Profilesmule:「ID Smule」\n" + \
                  "│➣ " + key + "Randomnumber:「Nmor-Nmor」\n" + \
                  "│➣ " + key + "Gimage:「Keyword」\n" + \
                  "│➣ " + key + "Img food:「Nama Makanan」\n" + \
                  "│➣ " + key + "Cekig:「ID IG」\n" + \
                  "│➣ " + key + "Profileig:「Nama IG」\n" + \
                  "│➣ " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "┝──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────"
    return helpMessage3
    
def helpsetting():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "╭──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────" + "\n" + \
                  "╭──────────────────" + "\n" + \
                  "│➣ ＨＥＬＰ ＳＥＴＴＩＮＧ" + "\n" + \
                  "┝──────────────────" + "\n" + \
                  "│➣ " + key + "Invite「on/off」\n" + \
                  "│➣ " + key + "Unsend「on/off」\n" + \
                  "│➣ " + key + "Jointicket「on/off」\n" + \
                  "│➣ " + key + "Sticker「on/off」\n" + \
                  "│➣ " + key + "Respon「on/off」\n" + \
                  "│➣ " + key + "Respongift「on/off」\n" + \
                  "│➣ " + key + "Contact「on/off」\n" + \
                  "│➣ " + key + "Autoleave「on/off」\n" + \
                  "│➣ " + key + "Autojoin「on/off」\n" + \
                  "│➣ " + key + "Autoadd「on/off」\n" + \
                  "│➣ " + key + "Autoblock「on/off」\n" + \
                  "│➣ " + key + "Checkpost「on/off」\n" + \
                  "│➣ " + key + "Read「on/off」\n" + \
                  "│➣ " + key + "Welcome「on/off」\n" + \
                  "│➣ " + key + "Simi「on/off」\n" + \
                  "│➣ " + key + "Mentionkick「on/off」\n" + \
                  "┝──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────"
    return helpMessage4
    
def helpprotect():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage5 = "╭──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────" + "\n" + \
                  "╭──────────────────" + "\n" + \
                  "│➣ ＨＥＬＰ ＰＲＯＴＥＣＴ" + "\n" + \
                  "┝──────────────────" + "\n" + \
                  "│➣ " + key + "Allpro「on/off」\n" + \
                  "│➣ " + key + "Prourl「on/off」\n" + \
                  "│➣ " + key + "Projoin「on/off」\n" + \
                  "│➣ " + key + "Prokick「on/off」\n" + \
                  "│➣ " + key + "Procancel「on/off」\n" + \
                  "│➣ " + key + "Procancel1「on/off」\n" + \
                  "│➣ " + key + "Proinvite「on/off」\n" + \
                  "│➣ " + key + "Antijs「on/off」\n" + \
                  "│➣ " + key + "Ghost「on/off」\n" + \
                  "│➣ " + key + "Pro Js\n" + \
                  "┝──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────"
    return helpMessage5
    
def helpadmin():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage6 = "╭──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────" + "\n" + \
                  "╭──────────────────" + "\n" + \
                  "│➣    ＨＥＬＰ ＡＤＭＩＮ" + "\n" + \
                  "┝──────────────────" + "\n" + \
                  "│➣ " + key + "Admin:on\n" + \
                  "│➣ " + key + "Admin:delete\n" + \
                  "│➣ " + key + "Staff:on\n" + \
                  "│➣ " + key + "Staff:delete\n" + \
                  "│➣ " + key + "Bot:on\n" + \
                  "│➣ " + key + "Bot:delete\n" + \
                  "│➣ " + key + "Adminadd「@」\n" + \
                  "│➣ " + key + "Admindell「@」\n" + \
                  "│➣ " + key + "Staffadd「@」\n" + \
                  "│➣ " + key + "Staffdell「@」\n" + \
                  "│➣ " + key + "Botadd「@」\n" + \
                  "│➣ " + key + "Botdell「@」\n" + \
                  "│➣ " + key + "Refresh\n" + \
                  "│➣ " + key + "Listbot\n" + \
                  "│➣ " + key + "Listadmin\n" + \
                  "│➣ " + key + "Listprotect\n" + \
                  "┝──────────────────" + "\n" + \
                  "│ ＳＥＬＦＢＯＴＢＹＭＡＸ" + "\n" + \
                  "╰──────────────────"
    return helpMessage6

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if aditmadzs.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            aditmadzs.reissueGroupTicket(op.param1)
                            X = aditmadzs.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            aditmadzs.updateGroup(X)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if k1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                k1.reissueGroupTicket(op.param1)
                                X = k1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                k1.updateGroup(X)
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if k2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    k2.reissueGroupTicket(op.param1)
                                    X = k2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    k2.updateGroup(X)
                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                    k2.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if k3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        k3.reissueGroupTicket(op.param1)
                                        X = k3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        k3.updateGroup(X)
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k3.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if k4.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            k4.reissueGroupTicket(op.param1)
                                            X = k4.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            k4.updateGroup(X)
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k4.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if k5.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                k5.reissueGroupTicket(op.param1)
                                                X = k5.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                k5.updateGroup(X)
                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                k5.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if k6.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    k6.reissueGroupTicket(op.param1)
                                                    X = k6.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    k6.updateGroup(X)
                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                    k6.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                        except:
                                            try:
                                                if k7.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        k7.reissueGroupTicket(op.param1)
                                                        X = k7.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        k7.updateGroup(X)
                                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                                        k7.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                            except:
                                                try:
                                                    if k8.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            k8.reissueGroupTicket(op.param1)
                                                            X = k8.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            k8.updateGroup(X)
                                                            k8.kickoutFromGroup(op.param1,[op.param2])
                                                            k8.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                except:
                                                    try:
                                                        if k9.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                k9.reissueGroupTicket(op.param1)
                                                                X = k9.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                k9.updateGroup(X)
                                                                k9.kickoutFromGroup(op.param1,[op.param2])
                                                                k9.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                    except:
                                                        try:
                                                            if k10.getGroup(op.param1).preventedJoinByTicket == False:
                                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                    k10.reissueGroupTicket(op.param1)
                                                                    X = k10.getGroup(op.param1)
                                                                    X.preventedJoinByTicket = True
                                                                    k10.updateGroup(X)
                                                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                                                    k10.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                        except:
                                                            pass                                                                   
#====================================================================
        if op.type == 13:
            if op.param3 in wait['blacklist'] and op.param2 in wait['blacklist'] and op.param2 not in Bots and op.param2 not in Saint and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                wait['blacklist'][op.param2] = True
                try:
                    k1.cancelGroupInvitation(op.param1,[op.param3])
                    k1.kickoutFromGroup(op.param1, [op.param2])
                except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k2.cancelGroupInvitation(op.param1,[op.param3])
                                k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.cancelGroupInvitation(op.param1,[op.param3])
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k4.cancelGroupInvitation(op.param1,[op.param3])
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k5.cancelGroupInvitation(op.param1,[op.param3])
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k6.cancelGroupInvitation(op.param1,[op.param3])
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    k7.cancelGroupInvitation(op.param1,[op.param3])
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        k8.cancelGroupInvitation(op.param1,[op.param3])
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            k9.cancelGroupInvitation(op.param1,[op.param3])
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                k10.cancelGroupInvitation(op.param1,[op.param3])
                                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                return

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.leaveGroup(op.param1)
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.leaveGroup(op.param1)
#====================================================================                          
        if op.type == 13:
            if mid in op.param3:
                G = aditmadzs.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    aditmadzs.acceptGroupInvitation(op.param1)
                    aditmadzs.sendMention(op.param1, wait["autoJoinMessage"], [op.param2])
                else:
                    if wait["autoJoin"] == True:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        aditmadzs.sendMention(op.param1, wait["autoJoinMessage"], [op.param2])
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            aditmadzs.cancelGroupInvitation(op.param1,[taged])
                        except:
                            pass

        if op.type == 13:
            if Amid in op.param3:
                G = k1.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k1.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k1.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k1.cancelGroupInvitation(op.param1,[taged])
                            k1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if Bmid in op.param3:
                G = k2.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k2.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k2.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k2.cancelGroupInvitation(op.param1,[taged])
                            k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if Cmid in op.param3:
                G = k3.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k3.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k3.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k3.cancelGroupInvitation(op.param1,[taged])
                            k3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if Dmid in op.param3:
                G = k4.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k4.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k4.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k4.cancelGroupInvitation(op.param1,[taged])
                            k4.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if Emid in op.param3:
                G = k5.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k5.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        ke.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k5.cancelGroupInvitation(op.param1,[taged])
                            k5.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if Fmid in op.param3:
                G = k6.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k6.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k6.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k6.cancelGroupInvitation(op.param1,[taged])
                            k6.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if Gmid in op.param3:
                G = k7.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k7.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k7.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k7.cancelGroupInvitation(op.param1,[taged])
                            k7.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if Hmid in op.param3:
                G = k8.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k8.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k8.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k8.cancelGroupInvitation(op.param1,[taged])
                            k8.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if Imid in op.param3:
                G = k9.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k9.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k9.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k9.cancelGroupInvitation(op.param1,[taged])
                            k9.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if Jmid in op.param3:
                G = k10.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    k10.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        k10.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            k10.cancelGroupInvitation(op.param1,[taged])
                            k10.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 13:
            if wait["autoJoin"] and mid in op.param3:
              group = aditmadzs.getGroup(op.param1)
              if wait["memberCancel"]["on"] == True:
                if len(group.members) <= wait["memberCancel"]["members"]:
                  aditmadzs.acceptGroupInvitation(op.param1)
                  aditmadzs.sendMention(op.param1, "Maaf aq leave krn membernya masih sedikit" ,[op.param2])
                  aditmadzs.leaveGroup(op.param1)
                else:
                  aditmadzs.acceptGroupInvitation(op.param1)
                  aditmadzs.sendMention(op.param1, wait["autoJoinMessage"], [op.param2])
                  aditmadzs.leaveGroup(op.param1)
#====================================================================       
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait['blacklist'][op.param2] = True
                    try:
                        group = k1.getGroup(op.param1)
                        inv1 = op.param3.replace('\x1e',',')
                        inv2 = inv1.split(',')
                        for target in inv2:
                            k1.cancelGroupInvitation(op.param1,[op.param3])
                            k1.kickoutFromGroup(op.param1, [op.param2])
                            wait["blacklist"][op.param2] = True
                    except:
                        try:
                            group = k2.getGroup(op.param1)
                            inv1 = op.param3.replace('\x1e',',')
                            inv2 = inv1.split(',')
                            for target in inv2:
                                k2.cancelGroupInvitation(op.param1,[op.param3])
                                k2.kickoutFromGroup(op.param1, [op.param2])
                                wait["blacklist"][op.param2] = True
                        except:
                            try:
                                group = k3.getGroup(op.param1)
                                inv1 = op.param3.replace('\x1e',',')
                                inv2 = inv1.split(',')
                                for target in inv2:
                                    k3.cancelGroupInvitation(op.param1,[op.param3])
                                    k3.kickoutFromGroup(op.param1, [op.param2])
                                    wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    group = k4.getGroup(op.param1)
                                    inv1 = op.param3.replace('\x1e',',')
                                    inv2 = inv1.split(',')
                                    for target in inv2:
                                        k4.cancelGroupInvitation(op.param1,[op.param3])
                                        k4.kickoutFromGroup(op.param1, [op.param2])
                                        wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        group = k5.getGroup(op.param1)
                                        inv1 = op.param3.replace('\x1e',',')
                                        inv2 = inv1.split(',')
                                        for target in inv2:
                                            k5.cancelGroupInvitation(op.param1,[op.param3])
                                            k5.kickoutFromGroup(op.param1, [op.param2])
                                            wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            group = k6.getGroup(op.param1)
                                            inv1 = op.param3.replace('\x1e',',')
                                            inv2 = inv1.split(',')
                                            for target in inv2:
                                                k6.cancelGroupInvitation(op.param1,[op.param3])
                                                k6.kickoutFromGroup(op.param1, [op.param2])
                                                wait["blacklist"][op.param2] = True
                                        except:
                                            try:
                                                group = k7.getGroup(op.param1)
                                                inv1 = op.param3.replace('\x1e',',')
                                                inv2 = inv1.split(',')
                                                for target in inv2:
                                                    k7.cancelGroupInvitation(op.param1,[op.param3])
                                                    k7.kickoutFromGroup(op.param1, [op.param2])
                                                    wait["blacklist"][op.param2] = True    
                                            except:
                                                try:
                                                   group = k8.getGroup(op.param1)
                                                   inv1 = op.param3.replace('\x1e',',')
                                                   inv2 = inv1.split(',')
                                                   for target in inv2:
                                                       k8.cancelGroupInvitation(op.param1,[op.param3])
                                                       k8.kickoutFromGroup(op.param1, [op.param2])
                                                       wait["blacklist"][op.param2] = True
                                                except:
                                                	pass       
#====================================================================       
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	k1.kickoutFromGroup(op.param1,[op.param2])
                    except: 
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                except: 
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                                                                
                return
#=====================================================================                            
        if op.type == 17:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	k1.kickoutFromGroup(op.param1,[op.param2])
                    except: 
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                except: 
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                                                                
                return                                                                         
#====================================================================
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                aditmadzs.findAndAddContactsByMid(op.param1)
            aditmadzs.sendMention(op.param1, wait["autoAddMessage"], [op.param1])

        if op.type == 5:
            if wait["autoBlock"] == True:
                aditmadzs.blockContact(op.param1)
            aditmadzs.sendMention(op.param1, wait["autoBlockMessage"], [op.param1])
#====================================================================                                            
        if op.type == 11:
            if op.param2 in wait['blacklist']:
                    try:
                        k1.reissueGroupTicket(op.param1) 
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k2.reissueGroupTicket(op.param1) 
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.reissueGroupTicket(op.param1) 
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k4.reissueGroupTicket(op.param1) 
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k5.reissueGroupTicket(op.param1) 
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k6.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    k7.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        k8.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            k9.reissueGroupTicket(op.param1)
                                                    except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                k10.reissueGroupTicket(op.param1)
                                                        except:
                                                            pass 
#====================================================================                            
        if op.type == 17:
            if op.param2 in wait['blacklist']:                
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2]) 
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
#====================================================================     
        if op.type == 19:
            if op.param2 in wait['blacklist']:            
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2]) 
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass                                                            
#====================================================================                                            
        if op.type == 19:
            try:
                if op.param1 in protectkick1:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    	wait["blacklist"][op.param2] = True
                    	try:
                            g1.acceptGroupInvitation(op.param1)
                            g1.inviteIntoGroup(op.param1,[op.param3])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            aditmadzs.acceptGroupInvitationByTicket(op.param1)
                    	except:
                          try:
                                G = g1.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                g1.updateGroup(G)
                                Ticket = g1.reissueGroupTicket(op.param1)
                                aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k10 .acceptGroupInvitationByTicket(op.param1,Ticket)
                                g1.kickoutFromGroup(op.param1,[op.param2])
                                g1.leaveGroup(op.param1)
                                X = aditmadzs.getGroup(op.param1)
                                X.preventeJoinByTicket = True
                                aditmadzs.updateGroup(X)
                                ginfo = aditmadzs.getGroup(msg.to)
                                aditmadzs.inviteIntoGroup(msg.to, [g1MID])
                                contact = aditmadzs.getContact(msg._from)
                                Ticket = aditmadzs.reissueGroupTicket(op.param1)
                                wait["blacklist"][op.param2] = True
                          except:
                              try:
                              	g1.inviteIntoGroup(op.param1,[op.param3])
                              	aditmadzs.acceptGroupInvitation(op.param1)
                              	g1.kickoutFromGroup(op.param1,[op.param2])
                              except:
                              	pass
						
                if op.param3 in g1MID:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[g1MID])
                        k1.sendMessage(op.param1,"AntiJS 1 Invited")
                    else:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[g1MID])
                        k1.sendMessage(op.param1,"AntiJS 1 Invited")
                                   
                if op.param3 in g1MID:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.findAndAddContactsByMid(op.param3)
                        k2.inviteIntoGroup(op.param1,[g1MID])
                        k2.sendMessage(op.param1,"AntiJS 2 Invited")
                    else:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.findAndAddContactsByMid(op.param3)
                        k2.inviteIntoGroup(op.param1,[g1MID])
                        k2.sendMessage(op.param1,"AntiJS 2 Invited")

                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).findAndAddContactsByMid(op.param3)
                            random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                            random.choice(ABC).sendMessage(op.param1,"Admin Invited")
                else:
                    pass
            except:
                pass
#=====================================================================                        
        if op.type == 19:
            if op.param1 in ghost:
            	try:
            	    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
            	        G = aditmadzs.getGroup(op.param1)
            	        G.preventedJoinByTicket = False
            	        aditmadzs.updateGroup(G)
            	        invsend = 0
            	        Ticket = aditmadzs.reissueGroupTicket(op.param1)
            	        g1.acceptGroupInvitationByTicket(op.param1,Ticket)
            	        try:
            	            g1.kickoutFromGroup(op.param1,[op.param2])
            	        except:
            	            try:
            	                g1.kickoutFromGroup(op.param1,[op.param2])
            	            except:
            	                pass
            	        wait["blacklist"][op.param2] = True
            	        try:
            	            g1.findAndAddContactsByMid(op.param3)
            	            g1.inviteIntoGroup(op.param1,[op.param3])
            	        except:
            	            try:
            	                g1.findAndAddContactsByMid(op.param3)
            	                g1.inviteIntoGroup(op.param1,[op.param3])
            	            except:
            	                g1.sendMessage(op.param1,"Blacklist succes")
            	                g1.leaveGroup(op.param1)
            	        g1.leaveGroup(op.param1)
            	        X = aditmadzs.getGroup(op.param1)
            	        X.preventedJoinByTicket = True
            	        aditmadzs.updateGroup(X)
            	except:
            	    pass              	
#=====================================================================                                    
        if op.type == 19:
            if op.param1 in protectantijs:
                if mid in op.param3:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        try:
                            g1.acceptGroupInvitation(op.param1)
                            g1.inviteIntoGroup(op.param1,[mid])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            aditmadzs.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                            g1.leaveGroup(op.param1)
                            aditmadzs.inviteIntoGroup(op.param1,[g1MID])
                        except:
                            pass              
#=====================================================================
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[g1MID])
                            k1.sendMessage(op.param1,"Heh Maen cancel cipok ni 👻")
                            k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)									
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[g1MID])
                                k2.sendMessage(op.param1,"Heh Maen cancel cipok ni 👻")
                                k2.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)										
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.inviteIntoGroup(op.param1,[g1MID])
                                    k3.sendMessage(op.param1,"Heh Maen cancel cipok ni 👻")
                                    k3.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)										
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[g1MID])
                                        k4.sendMessage(op.param1,"Heh Maen cancel cipok ni 👻")
                                        k4.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)											
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[g1MID])
                                            k5.sendMessage(op.param1,"Heh Maen cancel cipok ni 👻")
                                            k5.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                                k6.inviteIntoGroup(op.param1,[g1MID])
                                                k6.sendMessage(op.param1,"Heh Maen cancel cipok ni 👻")
                                                k6.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)			
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                                    k7.inviteIntoGroup(op.param1,[g1MID])
                                                    k7.sendMessage(op.param1,"Heh Maen cancel cipok ni 👻")
                                                    k7.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)														
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                        k8.nviteIntoGroup(op.param1,[g1MID])
                                                        k8.sendMessage(op.param1,"Heh Maen cancel cipok ni 👻")
                                                        k8.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)													
                                                except:
                                                    pass
                return
#====================================================================
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        aditmadzs.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            aditmadzs.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                aditmadzs.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k1.updateGroup(G)
                                    Ticket = k1.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    Ticket = k1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[op.param3])
                                        aditmadzs.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[op.param3])
                                            aditmadzs.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k2.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k2.updateGroup(G)
                                    Ticket = k2.reissueGroupTicket(op.param1)
                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                    Ticket = k2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[op.param3])
                                        k1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[op.param3])
                                            k1.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            k4.inviteIntoGroup(op.param1,[op.param3])
                            k2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                k2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k3.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k3.updateGroup(G)
                                    Ticket = k3.reissueGroupTicket(op.param1)
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k3.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k3.updateGroup(G)
                                    Ticket = k3.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[op.param3])
                                        k2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[op.param3])
                                            k2.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
                        k4.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            k5.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                k3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k4.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k4.updateGroup(G)
                                    Ticket = k4.reissueGroupTicket(op.param1)
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k4.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k4.updateGroup(G)
                                    Ticket = k4.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                        k3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[op.param3])
                                            k3.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k5.kickoutFromGroup(op.param1,[op.param2])
                        k5.inviteIntoGroup(op.param1,[op.param3])
                        k4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                k4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k5.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k5.updateGroup(G)
                                    Ticket = k5.reissueGroupTicket(op.param1)
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k5.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k5.updateGroup(G)
                                    Ticket = k5.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k2.kickoutFromGroup(op.param1,[op.param2])
                                        k2.inviteIntoGroup(op.param1,[op.param3])
                                        k4.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[op.param3])
                                            k4.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.inviteIntoGroup(op.param1,[op.param3])
                        k5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.inviteIntoGroup(op.param1,[op.param3])
                            k5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.inviteIntoGroup(op.param1,[op.param3])
                                k5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k6.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k6.updateGroup(G)
                                    Ticket = k6.reissueGroupTicket(op.param1)
                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k6.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k6.updateGroup(G)
                                    Ticket = k6.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k9.kickoutFromGroup(op.param1,[op.param2])
                                        k9.inviteIntoGroup(op.param1,[op.param3])
                                        k5.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                            k10.inviteIntoGroup(op.param1,[op.param3])
                                            k5.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
                        k7.inviteIntoGroup(op.param1,[op.param3])
                        k6.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.inviteIntoGroup(op.param1,[op.param3])
                            k6.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k9.kickoutFromGroup(op.param1,[op.param2])
                                k9.inviteIntoGroup(op.param1,[op.param3])
                                k6.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k7.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k7.updateGroup(G)
                                    Ticket = k7.reissueGroupTicket(op.param1)
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k7.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k7.updateGroup(G)
                                    Ticket = k7.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[op.param3])
                                        k6.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k10.kickoutFromGroup(op.param1,[op.param2])
                                            k10.inviteIntoGroup(op.param1,[op.param3])
                                            k6.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[op.param3])
                        k7.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k9.kickoutFromGroup(op.param1,[op.param2])
                            k9.inviteIntoGroup(op.param1,[op.param3])
                            k7.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k10.kickoutFromGroup(op.param1,[op.param2])
                                k10.inviteIntoGroup(op.param1,[op.param3])
                                k7.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k8.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k8.updateGroup(G)
                                    Ticket = k8.reissueGroupTicket(op.param1)
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k8.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k8.updateGroup(G)
                                    Ticket = k8.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k6.kickoutFromGroup(op.param1,[op.param2])
                                        k6.inviteIntoGroup(op.param1,[op.param3])
                                        k7.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[op.param3])
                                            k7.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k9.kickoutFromGroup(op.param1,[op.param2])
                        k9.inviteIntoGroup(op.param1,[op.param3])
                        k8.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k10.kickoutFromGroup(op.param1,[op.param2])
                            k10.inviteIntoGroup(op.param1,[op.param3])
                            k8.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                                k6.inviteIntoGroup(op.param1,[op.param3])
                                k8.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k9.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k9.updateGroup(G)
                                    Ticket = k9.reissueGroupTicket(op.param1)
                                    k9.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k9.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k9.updateGroup(G)
                                    Ticket = k9.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                        k8.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                            k8.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k10.kickoutFromGroup(op.param1,[op.param2])
                        k10.inviteIntoGroup(op.param1,[op.param3])
                        k9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k6.kickoutFromGroup(op.param1,[op.param2])
                            k6.inviteIntoGroup(op.param1,[op.param3])
                            k9.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k7.kickoutFromGroup(op.param1,[op.param2])
                                k7.inviteIntoGroup(op.param1,[op.param3])
                                k9.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k10.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k10.updateGroup(G)
                                    Ticket = k10.reissueGroupTicket(op.param1)
                                    k10.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k10.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k10.updateGroup(G)
                                    Ticket = k10.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                        k9.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k2.inviteIntoGroup(op.param1,[op.param3])
                                            k9.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        k10.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            k10.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                k10.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    k1.updateGroup(G)
                                    Ticket = k1.reissueGroupTicket(op.param1)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    Ticket = k1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[op.param3])
                                        k10.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.inviteIntoGroup(op.param1,[op.param3])
                                            k10.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["MAXreadPoint"]:
                   if op.param2 in Setmain["MAXreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["MAXreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = aditmadzs.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = aditmadzs.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        aditmadzs.sendImageWithURL(op.param1, image)                        
                                            
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Aditmadzs.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Aditmadzs.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                aditmadzs.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                                aditmadzs.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               aditmadzs.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass
                   
               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                           
                           
               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass
                   
               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                    

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])

               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, wait["Respontag"])
                           aditmadzs.sendMessage(msg.to, None, contentMetadata={"STKID":"21715710","STKPKGID":"9662","STKVER":"2"}, contentType=7)
                           break

               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           aditmadzs.sendMessage(msg.to, "Yang suka ngetag minta di gift yaa!?\nCek di chat, udah aku gift tuh...")
                           aditmadzs.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       

               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, "Jangan tag saya....")
                           aditmadzs.kickoutFromGroup(msg.to, [msg._from])
                           break

               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"「Cek ID Sticker」\n• STKID : " + msg.contentMetadata["STKID"] + "\n• STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n• STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"• Nama : " + msg.contentMetadata["displayName"] + "\n• MID : " + msg.contentMetadata["mid"] + "\n• Status : " + contact.statusMessage + "\n• Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = aditmadzs.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = aditmadzs.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}

            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nLink Sticker" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"• Nama : " + msg.contentMetadata["displayName"] + "\n• MID : " + msg.contentMetadata["mid"] + "\n• Status : " + contact.statusMessage + "\n• Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)

               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = aditmadzs.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            aditmadzs.sendMessage(msg.to, "「Dia ke bl kak... hpus bl dulu lalu invite lagi」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  aditmadzs.findAndAddContactsByMid(target)
                                  aditmadzs.inviteIntoGroup(msg.to,[target])
                                  ryan = aditmadzs.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 Sukses Invite 」\nNama "
                                  ret_ = "「Ketik Invite off jika sudah done」"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  aditmadzs.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  aditmadzs.sendText(msg.to,"Anda terkena limit")
                                  wait["invite"] = False
                                  break
#ADD BOT
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan anggota Aditmadzs BOT")
#ADD STAFFl
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = aditmadzs.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            aditmadzs.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = aditmadzs.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     aditmadzs.updateGroupPicture(msg.to, path)
                     aditmadzs.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["MAXfoto"]:
                            path = aditmadzs.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][mid]
                            aditmadzs.updateProfilePicture(path)
                            aditmadzs.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["MAXfoto"]:
                            path = k1.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Amid]
                            k1.updateProfilePicture(path)
                            k1.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["MAXfoto"]:
                            path = k2.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Bmid]
                            k2.updateProfilePicture(path)
                            k2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["MAXfoto"]:
                            path = k3.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Cmid]
                            k3.updateProfilePicture(path)
                            k3.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["MAXfoto"]:
                            path = k4.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Dmid]
                            k4.updateProfilePicture(path)
                            k4.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["MAXfoto"]:
                            path = k5.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Emid]
                            k5.updateProfilePicture(path)
                            k5.sendMessage(msg.to,"Foto berhasil dirubah")			
                        elif Fmid in Setmain["MAXfoto"]:
                            path = k6.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Fmid]
                            k6.updateProfilePicture(path)
                            k6.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Gmid in Setmain["MAXfoto"]:
                            path = k7.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Gmid]
                            k7.updateProfilePicture(path)
                            k7.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Hmid in Setmain["MAXfoto"]:
                            path = k8.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Hmid]
                            k8.updateProfilePicture(path)
                            k8.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Imid in Setmain["MAXfoto"]:
                            path = k9.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Imid]
                            k9.updateProfilePicture(path)
                            k9.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Jmid in Setmain["MAXfoto"]:
                            path = k10.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][Jmid]
                            k10.updateProfilePicture(path)
                            k10.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif g1MID in Setmain["MAXfoto"]:
                            path = g1.downloadObjectMsg(msg_id)
                            del Setmain["MAXfoto"][g1MID]
                            g1.updateProfilePicture(path)
                            g1.sendMessage(msg.to,"Foto berhasil dirubah")
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = k1.downloadObjectMsg(msg_id)
                     path2 = k2.downloadObjectMsg(msg_id)
                     path3 = k3.downloadObjectMsg(msg_id)	
                     path4 = k4.downloadObjectMsg(msg_id)
                     path5 = k5.downloadObjectMsg(msg_id)	
                     path6 = k6.downloadObjectMsg(msg_id)
                     path7 = k7.downloadObjectMsg(msg_id)
                     path8 = k8.downloadObjectMsg(msg_id)
                     path9 = k9.downloadObjectMsg(msg_id)
                     path10 = k10.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     k1.updateProfilePicture(path1)
                     k1.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k2.updateProfilePicture(path2)
                     k2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k3.updateProfilePicture(path3)
                     k3.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k4.updateProfilePicture(path4)
                     k4.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k5.updateProfilePicture(path5)
                     k5.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k6.updateProfilePicture(path6)
                     k6.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k7.updateProfilePicture(path7)
                     k7.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k8.updateProfilePicture(path8)
                     k8.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k9.updateProfilePicture(path9)
                     k9.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k10.updateProfilePicture(path10)
                     k10.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
               if msg.contentType == 0:
                    if wait["autoRead"] == True:
                        aditmadzs.sendChatChecked(msg.to, msg_id)
                        k1.sendChatChecked(msg.to, msg_id)
                        k2.sendChatChecked(msg.to, msg_id)
                        k3.sendChatChecked(msg.to, msg_id)
                        k4.sendChatChecked(msg.to, msg_id)
                        k5.sendChatChecked(msg.to, msg_id)
                        k6.sendChatChecked(msg.to, msg_id)
                        k7.sendChatChecked(msg.to, msg_id)
                        k8.sendChatChecked(msg.to, msg_id)
                        k9.sendChatChecked(msg.to, msg_id)
                        k10.sendChatChecked(msg.to, msg_id)
                        g1.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)                        
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               aditmadzs.sendReplyMessage(msg.id, to, str(helpMessage))

                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                aditmadzs.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                aditmadzs.sendMessage(msg.to, "Selfbot dinonaktifkan")

                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               aditmadzs.sendReplyMessage(msg.id, to, str(helpMessage1))
                                        
                        elif cmd == "help group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = helpgroup()
                               aditmadzs.sendReplyMessage(msg.id, to, str(helpMessage2))
                                                           
                        elif cmd == "help media":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = helpmedia()
                               aditmadzs.sendReplyMessage(msg.id, to, str(helpMessage3))
                                                                                
                        elif cmd == "help setting":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage4 = helpsetting()
                               aditmadzs.sendReplyMessage(msg.id, to, str(helpMessage4))
                                                           
                        elif cmd == "help protect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage5 = helpprotect()
                               aditmadzs.sendReplyMessage(msg.id, to, str(helpMessage5))
                                                           
                        elif cmd == "help admin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage6 = helpadmin()
                               aditmadzs.sendReplyMessage(msg.id, to, str(helpMessage6))

                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")                                

                        if cmd == "addbot":
                          if msg._from in admin:
                            try:
                                aditmadzs.findAndAddContactsByMid(Amid)
                                aditmadzs.findAndAddContactsByMid(Bmid)
                                aditmadzs.findAndAddContactsByMid(Cmid)
                                aditmadzs.findAndAddContactsByMid(Dmid)
                                aditmadzs.findAndAddContactsByMid(Emid)
                                aditmadzs.findAndAddContactsByMid(Fmid)
                                aditmadzs.findAndAddContactsByMid(Gmid)
                                aditmadzs.findAndAddContactsByMid(Hmid)
                                aditmadzs.findAndAddContactsByMid(Imid)
                                aditmadzs.findAndAddContactsByMid(Jmid)
                                aditmadzs.findAndAddContactsByMid(g1MID)
                                k1.findAndAddContactsByMid(mid)
                                k1.findAndAddContactsByMid(Bmid)
                                k1.findAndAddContactsByMid(Cmid)
                                k1.findAndAddContactsByMid(Dmid)
                                k1.findAndAddContactsByMid(Emid)
                                k1.findAndAddContactsByMid(Fmid)
                                k1.findAndAddContactsByMid(Gmid)
                                k1.findAndAddContactsByMid(Hmid)
                                k1.findAndAddContactsByMid(Imid)
                                k1.findAndAddContactsByMid(Jmid)
                                k1.findAndAddContactsByMid(g1MID)
                                k2.findAndAddContactsByMid(mid)
                                k2.findAndAddContactsByMid(Amid)
                                k2.findAndAddContactsByMid(Cmid)
                                k2.findAndAddContactsByMid(Dmid)
                                k2.findAndAddContactsByMid(Emid)
                                k2.findAndAddContactsByMid(Fmid)
                                k2.findAndAddContactsByMid(Gmid)
                                k2.findAndAddContactsByMid(Hmid)
                                k2.findAndAddContactsByMid(Imid)
                                k2.findAndAddContactsByMid(Jmid)
                                k2.findAndAddContactsByMid(g1MID)
                                k3.findAndAddContactsByMid(mid)
                                k3.findAndAddContactsByMid(Amid)
                                k3.findAndAddContactsByMid(Bmid)
                                k3.findAndAddContactsByMid(Dmid)
                                k3.findAndAddContactsByMid(Emid)
                                k3.findAndAddContactsByMid(Fmid)
                                k3.findAndAddContactsByMid(Gmid)
                                k3.findAndAddContactsByMid(Hmid)
                                k3.findAndAddContactsByMid(Imid)
                                k3.findAndAddContactsByMid(Jmid)
                                k3.findAndAddContactsByMid(g1MID)
                                k4.findAndAddContactsByMid(mid)
                                k4.findAndAddContactsByMid(Amid)
                                k4.findAndAddContactsByMid(Bmid)
                                k4.findAndAddContactsByMid(Cmid)
                                k4.findAndAddContactsByMid(Emid)
                                k4.findAndAddContactsByMid(Fmid)
                                k4.findAndAddContactsByMid(Gmid)
                                k4.findAndAddContactsByMid(Hmid)
                                k4.findAndAddContactsByMid(Imid)
                                k4.findAndAddContactsByMid(Jmid)
                                k4.findAndAddContactsByMid(g1MID)
                                k5.findAndAddContactsByMid(mid)
                                k5.findAndAddContactsByMid(Amid)
                                k5.findAndAddContactsByMid(Bmid)
                                k5.findAndAddContactsByMid(Cmid)
                                k5.findAndAddContactsByMid(Dmid)
                                k5.findAndAddContactsByMid(Fmid)
                                k5.findAndAddContactsByMid(Gmid)
                                k5.findAndAddContactsByMid(Hmid)
                                k5.findAndAddContactsByMid(Imid)
                                k5.findAndAddContactsByMid(Jmid)
                                k5.findAndAddContactsByMid(g1MID)
                                k6.findAndAddContactsByMid(mid)
                                k6.findAndAddContactsByMid(Amid)
                                k6.findAndAddContactsByMid(Bmid)
                                k6.findAndAddContactsByMid(Cmid)
                                k6.findAndAddContactsByMid(Dmid)
                                k6.findAndAddContactsByMid(Emid)
                                k6.findAndAddContactsByMid(Gmid)
                                k6.findAndAddContactsByMid(Hmid)
                                k6.findAndAddContactsByMid(Imid)
                                k6.findAndAddContactsByMid(Jmid)
                                k6.findAndAddContactsByMid(g1MID)
                                k7.findAndAddContactsByMid(mid)
                                k7.findAndAddContactsByMid(Amid)
                                k7.findAndAddContactsByMid(Bmid)
                                k7.findAndAddContactsByMid(Cmid)
                                k7.findAndAddContactsByMid(Dmid)
                                k7.findAndAddContactsByMid(Emid)
                                k7.findAndAddContactsByMid(Fmid)
                                k7.findAndAddContactsByMid(Hmid)
                                k7.findAndAddContactsByMid(Imid)
                                k7.findAndAddContactsByMid(Jmid)
                                k7.findAndAddContactsByMid(g1MID)                                
                                k8.findAndAddContactsByMid(mid)
                                k8.findAndAddContactsByMid(Amid)
                                k8.findAndAddContactsByMid(Bmid)
                                k8.findAndAddContactsByMid(Cmid)
                                k8.findAndAddContactsByMid(Dmid)
                                k8.findAndAddContactsByMid(Emid)
                                k8.findAndAddContactsByMid(Fmid)
                                k8.findAndAddContactsByMid(Gmid)
                                k8.findAndAddContactsByMid(Imid)
                                k8.findAndAddContactsByMid(Jmid)
                                k8.findAndAddContactsByMid(g1MID)
                                k9.findAndAddContactsByMid(mid)
                                k9.findAndAddContactsByMid(Amid)
                                k9.findAndAddContactsByMid(Bmid)
                                k9.findAndAddContactsByMid(Cmid)
                                k9.findAndAddContactsByMid(Dmid)
                                k9.findAndAddContactsByMid(Emid)
                                k9.findAndAddContactsByMid(Fmid)
                                k9.findAndAddContactsByMid(Gmid)
                                k9.findAndAddContactsByMid(Hmid)
                                k9.findAndAddContactsByMid(Jmid)
                                k9.findAndAddContactsByMid(g1MID)
                                k10.findAndAddContactsByMid(mid)
                                k10.findAndAddContactsByMid(Amid)
                                k10.findAndAddContactsByMid(Bmid)
                                k10.findAndAddContactsByMid(Cmid)
                                k10.findAndAddContactsByMid(Dmid)
                                k10.findAndAddContactsByMid(Emid)
                                k10.findAndAddContactsByMid(Fmid)
                                k10.findAndAddContactsByMid(Gmid)
                                k10.findAndAddContactsByMid(Hmid)
                                k10.findAndAddContactsByMid(Imid)
                                k10.findAndAddContactsByMid(g1MID)
                                g1.findAndAddContactsByMid(mid)
                                g1.findAndAddContactsByMid(Amid)
                                g1.findAndAddContactsByMid(Bmid)
                                g1.findAndAddContactsByMid(Cmid)
                                g1.findAndAddContactsByMid(Dmid)
                                g1.findAndAddContactsByMid(Emid)
                                g1.findAndAddContactsByMid(Fmid)
                                g1.findAndAddContactsByMid(Gmid)
                                g1.findAndAddContactsByMid(Hmid)
                                g1.findAndAddContactsByMid(Imid)
                                g1.findAndAddContactsByMid(Jmid)
                                aditmadzs.sendMessage(to,"Has added a bot friend successfully.")
                            except:
                                aditmadzs.sendMessage(to,"Has added a bot friend successfully.")

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭≻「 Status Protect 」\n"
                                if wait["unsend"] == True: md+="├≻ Unsend「On」\n"
                                else: md+="├≻ Unsend「Off」\n"
                                if wait["Mentionkick"] == True: md+="├≻ Mentionkick「On」\n"
                                else: md+="├≻ Mentionkick「Off」\n"
                                if wait["Mentiongift"] == True: md+="├≻ Mentiongift「On」\n"
                                else: md+="├≻ Mentiongift「Off」\n"
                                if wait["detectMention"] == True: md+="├≻ Respon「On」\n"
                                else: md+="├≻ Respon「Off」\n"                   
                                if wait["autoJoin"] == True: md+="├≻ Autojoin「On」\n"
                                else: md+="├≻ Autojoin「Off」\n"
                                if settings["autoJoinTicket"] == True: md+="├≻ Jointicket「On」\n"
                                else: md+="├≻ Jointicket「Off」\n"                                
                                if wait["autoAdd"] == True: md+="├≻ Autoadd「On」\n"
                                else: md+="├≻ Autoadd「Off」\n"                   
                                if wait["autoBlock"] == True: md+="├≻ AutoBlock「On」\n"
                                else: md+="├≻ AutoBlock「Off」\n"
                                if msg.to in welcome: md+="├≻ Welcome「On」\n"
                                else: md+="├≻ Welcome「Off」\n"                 
                                if wait["autoLeave"] == True: md+="├≻ Autoleave「On」\n"
                                else: md+="├≻ Autoleave「Off」\n"
                                if msg.to in protectqr: md+="├≻ Protecturl「On」\n"
                                else: md+="├≻ Protecturl「Off」\n"
                                if msg.to in protectjoin: md+="├≻ ProtectJoin「On」\n"
                                else: md+="├≻ ProtectJoin「Off」\n"
                                if msg.to in protectkick: md+="├≻ Protectkick「On」\n"
                                else: md+="├≻ Protectkick「Off」\n"
                                if msg.to in protectcancel: md+="├≻ Protectcancel「On」\n"
                                else: md+="├≻ Protectcancel「Off」\n"
                                if msg.to in protectinvite: md+="├≻ Protectinvite「On」\n"
                                else: md+="├≻ Protectinvite「Off」\n"
                                if msg.to in protectantijs: md+="├≻ Antijs「On」\n"
                                else: md+="├≻ Antijs「Off」\n"  
                                if msg.to in ghost: md+="├≻ Ghost「On」\n"
                                else: md+="├≻ Ghost「Off」\n"
                                aditmadzs.sendReplyMessage(msg.id, to, md+"├──────────────\n├≻ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n├≻ Jam :! "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╰≻「 Selfbot Protect 」")

                        elif cmd == "kickall":
                          if msg._from in admin or msg._from in Bots:
                            if msg.toType != 2: return aditmadzs.sendMessage(to, 'Failed kick all members, use this command only on group chat')
                            group = aditmadzs.getCompactGroup(to)
                            if not group.members:
                                return aditmadzs.sendMessage(to, 'Failed kick all members, no member in list')
                            for member in group.members:
                                if member.mid == mid:
                                    continue
                                try:
                                    aditmadzs.kickoutFromGroup(to, [member.mid])
                                except TalkException as talk_error:
                                    return aditmadzs.sendMessage(to, 'Failed kick all members, the reason is `%s`' % talk_error.reason)
                                time.sleep(0.8)
                            aditmadzs.sendMessage(to, 'Success kick all members, totals %i members' % len(group.members))

                        elif cmd == "krandom":
                          if msg._from in admin or msg._from in Bots:
                            if msg.toType != 2: return random.choice(ABC).sendMessage(to, 'Failed kick all members, use this command only on group chat')
                            group = aditmadzs.getCompactGroup(to)
                            if not group.members:
                                return random.choice(ABC).sendMessage(to, 'Failed kick all members, no member in list')
                            for member in group.members:
                                if member.mid == mid:
                                    continue
                                try:
                                    random.choice(ABC).kickoutFromGroup(to, [member.mid])
                                except TalkException as talk_error:
                                    return random.choice(ABC).sendMessage(to, 'Failed kick all members, the reason is `%s`' % talk_error.reason)
                                time.sleep(0.2)
                            random.choice(ABC).sendMessage(to, 'Success kick all members, totals %i members' % len(group.members))

                        elif cmd == "cancelall":
                          if msg._from in admin or msg._from in Bots:
                            if msg.toType != 2: return aditmadzs.sendMessage(to, 'Failed cancel all pending members, use this command only on group chat')
                            group = aditmadzs.getCompactGroup(to)
                            if not group.invitee:
                                return aditmadzs.sendMessage(to, 'Failed cancel all pending members, no pending member in list')
                            for member in group.invitee:
                                if member.mid == mid:
                                    continue
                                try:
                                    aditmadzs.cancelGroupInvitation(to, [member.mid])
                                except TalkException as talk_error:
                                    return aditmadzs.sendMessage(to, 'Failed cancel all pending members, the reason is `%s`' % talk_error.reason)
                                time.sleep(0.8)
                            aditmadzs.sendMessage(to, 'Success cancel all pending members, totals %i pending members' % len(pendings))

                        elif cmd == "crandom":
                          if msg._from in admin or msg._from in Bots:
                            if msg.toType != 2: return random.choice(ABC).sendMessage(to, 'Failed cancel all pending members, use this command only on group chat')
                            group = aditmadzs.getCompactGroup(to)
                            if not group.invitee:
                                return random.choice(ABC).sendMessage(to, 'Failed cancel all pending members, no pending member in list')
                            for member in group.invitee:
                                if member.mid == mid:
                                    continue
                                try:
                                    random.choice(ABC).cancelGroupInvitation(to, [member.mid])
                                except TalkException as talk_error:
                                    return random.choice(ABC).sendMessage(to, 'Failed cancel all pending members, the reason is `%s`' % talk_error.reason)
                                time.sleep(0.3)
                            random.choice(ABC).sendMessage(to, 'Success cancel all pending members, totals %i pending members' % len(pendings))

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                aditmadzs.sendMessage(msg.to,"Bot Creator") 
                                ma = ""
                                for i in creator:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "SelfBOT 20 Assist\n")
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
       
                        elif cmd == "me":
                          if msg._from in admin:
                            if msg.toType == 0:
                                aditmadzs.generateReplyMessage(msg.id)
                                aditmadzs.sendReplyMessage(msg_id, to, aditmadzs.getContact(sender).displayName, contentMetadata = {'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(to).pictureStatus, 'MSG_SENDER_NAME': aditmadzs.getContact(to).displayName, 'previewUrl': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~max_pv', 'type': 'mt', 'subText': ""+aditmadzs.getContact(sender).statusMessage, 'a-installUrl': 'https://line.me/ti/p/~max_pv', 'a-installUrl': ' https://line.me/ti/p/~max_pv', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~max_pv', 'i-linkUri': 'https://line.me/ti/p/~max_pv', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~max_pv'}, contentType=19)
                            else:
                                aditmadzs.sendReplyMessage(msg_id, to, aditmadzs.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~'+aditmadzs.getProfile().userid, 'type': 'mt', 'subText': ""+aditmadzs.getContact(sender).statusMessage, 'a-installUrl': 'https://line.me/ti/p/~max_pv', 'a-installUrl': ' https://line.me/ti/p/~max_pv', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~max_pv', 'i-linkUri': 'https://line.me/ti/p/~max_pv', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~max_pv'}, contentType=19)

                        elif cmd == 'me1':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               aditmadzs.sendReplyMessage(msg_id, to, None, contentMetadata={'mid': msg._from}, contentType=13)
                               path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath

                        elif text.lower() == "mid":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendReplyMessage(msg_id, to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               aditmadzs.sendReplyMessage(msg_id, to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendReplyMessage(msg.to, "• Nama : "+str(mi.displayName)+"\n• Mid : " +key1+"\n• Status : "+str(mi.statusMessage))
                               aditmadzs.sendReplyMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(aditmadzs.getContact(key1)):
                                   aditmadzs.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   aditmadzs.sendReplyImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == 'gift':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               aditmadzs.generateReplyMessage(msg.id)
                               aditmadzs.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '6'}, contentType=9)   
                               k1.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '1'}, contentType=9)   
                               k2.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '2'}, contentType=9)   
                               k3.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '3'}, contentType=9)   
                               k4.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '4'}, contentType=9)   
                               k5.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)   
                               k6.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '4'}, contentType=9)   
                               k7.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '3'}, contentType=9)   
                               k8.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '1'}, contentType=9)   
                               k9.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '2'}, contentType=9)   
                               k10.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '3'}, contentType=9)   

                        elif cmd  == "mid all":
                          if msg._from in admin:
                              aditmadzs.sendReplyMessage(msg_id, to,mid)
                              k1.sendReplyMessage(msg_id, to,Amid)
                              k2.sendReplyMessage(msg_id, to,Bmid)
                              k3.sendReplyMessage(msg_id, to,Cmid)
                              k4.sendReplyMessage(msg_id, to,Dmid)
                              k5.sendReplyMessage(msg_id, to,Emid)
                              k6.sendReplyMessage(msg_id, to,Fmid)
                              k7.sendReplyMessage(msg_id, to,Gmid)
                              k8.sendReplyMessage(msg_id, to,Hmid)
                              k9.sendReplyMessage(msg_id, to,Imid)
                              k10.sendReplyMessage(msg_id, to,Jmid)

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': mid}, contentType=13)
                               msg.contentMetadata = {'mid': Amid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Amid}, contentType=13)
                               msg.contentMetadata = {'mid': Bmid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Bmid}, contentType=13)
                               msg.contentMetadata = {'mid': Cmid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Cmid}, contentType=13)
                               msg.contentMetadata = {'mid': Dmid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Dmid}, contentType=13)
                               msg.contentMetadata = {'mid': Emid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Emid}, contentType=13)
                               msg.contentMetadata = {'mid': Fmid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Fmid}, contentType=13)
                               msg.contentMetadata = {'mid': Gmid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Gmid}, contentType=13)
                               msg.contentMetadata = {'mid': Hmid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Hmid}, contentType=13)
                               msg.contentMetadata = {'mid': Imid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Imid}, contentType=13)
                               msg.contentMetadata = {'mid': Jmid}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': Jmid}, contentType=13)
                               msg.contentMetadata = {'mid': g1MID}
                               aditmadzs.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': g1MID}, contentType=13)
                                
                        elif cmd == "cek":
                            if msg._from in admin:
                                try:k1.inviteIntoGroup(to, ["uede82bce02e6eb6ad7e23e69af82a64a"]);has = "OK"
                                except:has = "NOT"
                                try:k1.kickoutFromGroup(to, ["uede82bce02e6eb6ad7e23e69af82a64a"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k1.sendReplyMessage(msg_id, to, "• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:k2.inviteIntoGroup(to, ["ucd19475865ae005c6a4a30a6fea50608"]);has = "OK"
                                except:has = "NOT"
                                try:k2.kickoutFromGroup(to, ["ucd19475865ae005c6a4a30a6fea50608"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k2.sendReplyMessage(msg_id, to, "• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:k3.inviteIntoGroup(to, ["uef1c3d99993da6dfa0402b002a6da1cb"]);has = "OK"
                                except:has = "NOT"
                                try:k3.kickoutFromGroup(to, ["uef1c3d99993da6dfa0402b002a6da1cb"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k3.sendReplyMessage(msg_id, to, "• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:k4.inviteIntoGroup(to, ["u1103a34a6d364380d7d45978cd81f8d8"]);has = "OK"
                                except:has = "NOT"
                                try:k4.kickoutFromGroup(to, ["u1103a34a6d364380d7d45978cd81f8d8"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k4.sendReplyMessage(msg_id, to,"• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:k5.inviteIntoGroup(to, ["uaa609044e80922b07ea87dfa1ff8baf0"]);has = "OK"
                                except:has = "NOT"
                                try:k5.kickoutFromGroup(to, ["uaa609044e80922b07ea87dfa1ff8baf0"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k5.sendReplyMessage(msg_id, to, "• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:k6.inviteIntoGroup(to, ["ua00989ff6bd62961dd76a54ccf086d51"]);has = "OK"
                                except:has = "NOT"
                                try:k6.kickoutFromGroup(to, ["ua00989ff6bd62961dd76a54ccf086d51"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k6.sendReplyMessage(msg_id, to, "• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:k7.inviteIntoGroup(to, ["u2ae08648177dbdc700feff3a10c6ef78"]);has = "OK"
                                except:has = "NOT"
                                try:k7.kickoutFromGroup(to, ["u2ae08648177dbdc700feff3a10c6ef78"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k7.sendReplyMessage(msg_id, to, "• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:k8.inviteIntoGroup(to, ["u8233b3e518a8922a83886180f9112e37"]);has = "OK"
                                except:has = "NOT"
                                try:k8.kickoutFromGroup(to, ["u8233b3e518a8922a83886180f9112e37"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k8.sendReplyMessage(msg_id, to, "• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:k9.inviteIntoGroup(to, ["u14dfe063cb3fb4c56b6f2e30c9e8f690"]);has = "OK"
                                except:has = "NOT"
                                try:k9.kickoutFromGroup(to, ["u14dfe063cb3fb4c56b6f2e30c9e8f690"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k9.sendReplyMessage(msg_id, to, "• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                                try:k10.inviteIntoGroup(to, ["u2b01a3ca76465b07db87f611f00c8620"]);has = "OK"
                                except:has = "NOT"
                                try:k10.kickoutFromGroup(to, ["u2b01a3ca76465b07db87f611f00c8620"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "ɴᴏʀᴍᴀʟ"
                                else:sil = "ʟɪᴍɪᴛ "
                                if has1 == "OK":sil1 = "ɴᴏʀᴍᴀʟ"
                                else:sil1 = "ʟɪᴍɪᴛ "
                                k10.sendReplyMessage(msg_id, to, "• ᴄᴇᴋ ʟɪᴍɪᴛ ʙᴏᴛ\n\n• ᴋɪᴄᴋ : {} \n• ɪɴᴠɪᴛᴇ : {}".format(sil1,sil))

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   aditmadzs.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   k1.removeAllMessages(op.param2)
                                   k1.sendMessage(msg.to,"Deleted chat messages successfully")
                                   k2.removeAllMessages(op.param2)
                                   k2.sendMessage(msg.to,"Deleted chat messages successfully")
                                   k3.removeAllMessages(op.param2)
                                   k3.sendMessage(msg.to,"Deleted chat messages successfully")
                                   k4.removeAllMessages(op.param2)
                                   k4.sendMessage(msg.to,"Deleted chat messages successfully")
                                   k5.removeAllMessages(op.param2)
                                   k5.sendMessage(msg.to,"Deleted chat messages successfully")
                                   k6.removeAllMessages(op.param2)	
                                   k6.sendMessage(msg.to,"Deleted chat messages successfully")
                                   k7.removeAllMessages(op.param2)	
                                   k7.sendMessage(msg.to,"Deleted chat messages successfully")
                                   k8.removeAllMessages(op.param2)	
                                   k8.sendMessage(msg.to,"Deleted chat messages successfully")
                                   k9.removeAllMessages(op.param2)	
                                   k9.sendMessage(msg.to,"Deleted chat messages successfully")
                                   k10.removeAllMessages(op.param2)	
                                   k10.sendMessage(msg.to,"Deleted chat messages successfully")
                                   g1.removeAllMessages(op.param2)		
                                   aditmadzs.sendMessage(msg.to,"Deleted chat messages successfully")
                               except:
                                   pass

                        elif cmd == "myname":
                          if msg._from in owner or admin:
                            contact = aditmadzs.getContact(sender)
                            aditmadzs.sendMention(to, "@!\n{}".format(contact.displayName), [sender])

                        elif cmd == "mybio":
                          if msg._from in owner or admin:
                            contact = aditmadzs.getContact(sender)
                            aditmadzs.sendMention(to, "@!\n{}".format(contact.statusMessage), [sender])

                        elif cmd == "mypicture":
                          if msg._from in owner or admin:
                            contact = aditmadzs.getContact(sender)
                            aditmadzs.sendReplyImageWithURL(msg_id, to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                        elif cmd == "myvideoprofile":
                          if msg._from in owner or admin:
                            contact = aditmadzs.getContact(sender)
                            if contact.videoProfile == None:
                                return aditmadzs.sendMessage(to, "Anda tidak memiliki video profile")
                            aditmadzs.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                        elif cmd == "mycover":
                          if msg._from in owner or admin:
                            cover = aditmadzs.getProfileCoverURL(sender)
                            aditmadzs.sendImageWithURL(to, str(cover))

                        elif cmd == "mycover url":
                          if msg._from in owner or admin:
                            cover = aditmadzs.getProfileCoverURL(sender)
                            aditmadzs.sendMessage(to, str(cover))

                        elif cmd.startswith("changegroupname: "):
                          if msg._from in owner or admin:
                            if msg.toType == 2:
                                sep = text.split(" ")
                                groupname = text.replace(sep[0] + " ","")
                                if len(groupname) <= 100:
                                    group = aditmadzs.getGroup(to)
                                    group.name = groupname
                                    aditmadzs.updateGroup(group)
                                    aditmadzs.sendMessage(to, "Berhasil mengubah nama group menjadi : {}".format(groupname))

                        elif cmd.startswith("getcover "):
                          if msg._from in owner or admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cover = aditmadzs.getProfileCoverURL(ls)
                                    aditmadzs.sendImageWithURL(to, str(cover))

                        elif cmd.startswith("friendbc: "):
                          if msg._from in owner or admin:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            contacts = aditmadzs.getAllContactIds()
                            for contact in contacts:
                                aditmadzs.sendMessage(contact, "「 Bᵣₒₐdcₐₛₜ 」\n{}".format(str(txt)))
                            aditmadzs.sendMessage(msg.to, "Bₑᵣₕₐₛᵢₗ bᵣₒₐdcₐₛₜ ₖₑ {} ₜₑₘₐₙ".format(str(len(contacts))))

                        elif cmd.startswith("groupbc: "):
                          if msg._from in owner or admin:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            for group in groups:
                                aditmadzs.sendMessage(group, "「 Bᵣₒₐdcₐₛₜ 」\n{}".format(str(txt)))
                            aditmadzs.sendMessage(msg.to, "Bₑᵣₕₐₛᵢₗ bᵣₒₐdcₐₛₜ ₖₑ {} gᵣₒᵤₚ".format(str(len(groups))))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   aditmadzs.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   aditmadzs.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               aditmadzs.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               aditmadzs.sendMessage(msg.to, "Restart Sukses Bos!...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Bot waktu kerja " +waktu(eltime)
                               aditmadzs.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = aditmadzs.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                aditmadzs.sendReplyMessage(msg_id, to, "• Grup Info\n\n• Nama Group : {}".format(G.name)+ "\n• ID Group : {}".format(G.id)+ "\n• Pembuat : {}".format(G.creator.displayName)+ "\n• Waktu Dibuat : {}".format(str(timeCreated))+ "\n• Jumlah Member : {}".format(str(len(G.members)))+ "\n• Jumlah Pending : {}".format(gPending)+ "\n• Group Qr : {}".format(gQr)+ "\n• Group Ticket : {}".format(gTicket))
                                aditmadzs.sendReplyMessage(msg_id, to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                aditmadzs.sendReplyImageWithURL(msg_id, to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "• BOT Grup Info\n"
                                ret_ += "\n• Name : {}".format(G.name)
                                ret_ += "\n• ID : {}".format(G.id)
                                ret_ += "\n• Creator : {}".format(gCreator)
                                ret_ += "\n• Created Time : {}".format(str(timeCreated))
                                ret_ += "\n• Member : {}".format(str(len(G.members)))
                                ret_ += "\n• Pending : {}".format(gPending)
                                ret_ += "\n• Qr : {}".format(gQr)
                                ret_ += "\n• Ticket : {}".format(gTicket)
                                ret_ += ""
                                aditmadzs.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "• "+ str(no) + ". " + mem.displayName
                                aditmadzs.sendMessage(to,"• Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass
#GROUP
                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = aditmadzs.getGroup(i)
                                if ginfo == group:
                                    aditmadzs.leaveGroup(i)
                                    aditmadzs.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd.startswith("leavegroup: "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    h = aditmadzs.getGroup(i).name
                                    if h == ng:
                                        aditmadzs.leaveGroup(i)

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getAllContactIds()
                               for i in gid:
                                   G = aditmadzs.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├≽ " + str(a) + ". " +G.displayName+ "\n"
                               aditmadzs.sendMessage(msg.to,"╭───「 Friend List 」\n"+ma+"╰───「 Total "+str(len(gid))+" Friends 」")

                        elif cmd == "all mid":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                num = 0
                                ret_ = "╭───「 Mid List On Group {} 」".format(group.name)
                                for contact in group.members:
                                    num += 1
                                    ret_ += "\n├≽ {}.{}\n├{}".format(num, contact.displayName, contact.mid)
                                ret_ += "\n╰───「 Total {} Members 」".format(len(group.members))
                                aditmadzs.sendReplyMessage(msg_id, to, ret_)

                        elif cmd == "pendinglist":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                ret_ = "╭───「 Pending List 」"
                                no = 0
                                if group.invitee is None or group.invitee == []:
                                    return aditmadzs.sendReplyMessage(msg_id, to, "Tidak ada pendingan")
                                else:
                                    for pending in group.invitee:
                                        no += 1
                                        ret_ += "\n├≽ {}. {}".format(str(no), str(pending.displayName))
                                    ret_ += "\n╰───「 Total {} Pending 」".format(str(len(group.invitee)))
                                    aditmadzs.sendReplyMessage(msg_id, to, str(ret_))

                        elif cmd == "memberlist":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                num = 0
                                ret_ = "╭───「 Member List 」"
                                for contact in group.members:
                                    num += 1
                                    ret_ += "\n├≽ {}. {}".format(num, contact.displayName)
                                ret_ += "\n╰───「 Total {} Members 」".format(len(group.members))
                                aditmadzs.sendReplyMessage(msg_id, to, ret_)

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getGroupIdsJoined()
                               for i in gid:
                                   G = aditmadzs.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├≽ " + str(a) + ". " +G.name+ "\n"
                               aditmadzs.sendMessage(msg.to,"╭───「 Groups List 」\n"+ma+"╰───「 Total "+str(len(gid))+" Groups 」")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = k1.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├≽ " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"╭───「 Groups List Bot 」\n"+ma+"╰───「 Total "+str(len(gid))+" Groups 」")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = aditmadzs.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   aditmadzs.updateGroup(X)
                                   aditmadzs.sendMessage(msg.to, "Berhasil menambahkan qr")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = aditmadzs.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   aditmadzs.updateGroup(X)
                                   aditmadzs.sendMessage(msg.to, "Hapus qr Berhasil")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = aditmadzs.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      aditmadzs.updateGroup(x)
                                   gurl = aditmadzs.reissueGroupTicket(msg.to)
                                   aditmadzs.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                              
                        elif cmd == "clear spam":
                          if msg._from in admin:
                            ginvited = aditmadzs.getGroupIdsInvited()
                            if ginvited != [] and ginvited != None:
                                for gid in ginvited:
                                    aditmadzs.acceptGroupInvitation(gid)
                                    aditmadzs.leaveGroup(gid)
                                aditmadzs.sendMessage(to, " Succes Reject {} Group Invite".format(str(len(ginvited))))
                            else:
                                aditmadzs.sendMessage(to, "Nothing")
                                   
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = aditmadzs.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      aditmadzs.rejectGroupInvitation(gid)
                                  aditmadzs.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  aditmadzs.sendMessage(to, "Tidak ada undangan yang tertunda")
#UPDATE FOTO
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["MAXfoto"][mid] = True
                                aditmadzs.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "1up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Amid] = True
                                k1.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})

                        elif cmd == "2up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Bmid] = True
                                k2.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
                                
                        elif cmd == "3up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Cmid] = True
                                k3.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})

                        elif cmd == "4up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Dmid] = True
                                k4.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "5up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Emid] = True
                                k5.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "6up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Fmid] = True
                                k6.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "7up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Gmid] = True
                                k7.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "8up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Hmid] = True
                                k8.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "9up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Imid] = True
                                k9.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
								
                        elif cmd == "10up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][Jmid] = True
                                k10.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})

                        elif cmd == "11up":
                            if msg._from in admin:
                                Setmain["MAXfoto"][g1MID] = True
                                g1.sendMessage(msg.to,"Kirim fotonya.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/~max_pv'})
#UPDATE ALL NAME
                        elif cmd.startswith("allname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 50:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k4.getProfile()
                                profile.displayName = string
                                k4.updateProfile(profile)
                                k4.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k5.getProfile()
                                profile.displayName = string
                                k5.updateProfile(profile)
                                k5.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k6.getProfile()
                                profile.displayName = string
                                k6.updateProfile(profile)
                                k6.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k7.getProfile()
                                profile.displayName = string
                                k7.updateProfile(profile)
                                k7.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k8.getProfile()
                                profile.displayName = string
                                k8.updateProfile(profile)
                                k8.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k9.getProfile()
                                profile.displayName = string
                                k9.updateProfile(profile)
                                k9.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                profile = k10.getProfile()
                                profile.displayName = string
                                k10.updateProfile(profile)
                                k10.sendMessage(msg.to,"Nama diganti jadi " + string + "")
#UPDATE STATUS
                        elif "bio: " in msg.text.lower():
                           if msg._from in admin:
                              proses = text.split(": ")
                              string = text.replace(proses[0] + ": ","")
                              profile_A = aditmadzs.getProfile()
                              profile_A.statusMessage = string
                              aditmadzs.updateProfile(profile_A)
                              aditmadzs.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k1.getProfile()
                              profile_A.statusMessage = string
                              k1.updateProfile(profile_A)
                              k1.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k2.getProfile()
                              profile_A.statusMessage = string
                              k2.updateProfile(profile_A)
                              k2.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k3.getProfile()
                              profile_A.statusMessage = string
                              k3.updateProfile(profile_A)
                              k3.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k4.getProfile()
                              profile_A.statusMessage = string
                              k4.updateProfile(profile_A)
                              k4.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k5.getProfile()
                              profile_A.statusMessage = string
                              k5.updateProfile(profile_A)
                              k5.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k6.getProfile()
                              profile_A.statusMessage = string
                              k6.updateProfile(profile_A)
                              k6.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k7.getProfile()
                              profile_A.statusMessage = string
                              k7.updateProfile(profile_A)
                              k7.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k8.getProfile()
                              profile_A.statusMessage = string
                              k8.updateProfile(profile_A)
                              k8.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k9.getProfile()
                              profile_A.statusMessage = string
                              k9.updateProfile(profile_A)
                              k9.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = k10.getProfile()
                              profile_A.statusMessage = string
                              k10.updateProfile(profile_A)
                              k10.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
                              profile_A = g1.getProfile()
                              profile_A.statusMessage = string
                              g1.updateProfile(profile_A)
                              g1.sendReplyMessage(msg_id, to,"Bio diganti jadi " + string)
#UPDATE NAME
                        elif cmd.startswith("name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = aditmadzs.getProfile()
                                profile.displayName = string
                                aditmadzs.updateProfile(profile)
                                aditmadzs.sendReplyMessage(msg_id, to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k4.getProfile()
                                profile.displayName = string
                                k4.updateProfile(profile)
                                k4.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k5.getProfile()
                                profile.displayName = string
                                k5.updateProfile(profile)
                                k5.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k6.getProfile()
                                profile.displayName = string
                                k6.updateProfile(profile)
                                k6.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k7.getProfile()
                                profile.displayName = string
                                k7.updateProfile(profile)
                                k7.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k8.getProfile()
                                profile.displayName = string
                                k8.updateProfile(profile)
                                k8.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k9.getProfile()
                                profile.displayName = string
                                k9.updateProfile(profile)
                                k9.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k10.getProfile()
                                profile.displayName = string
                                k10.updateProfile(profile)
                                k10.sendMessage(msg.to,"Nama diganti jadi " + string + "")
								
                        elif cmd.startswith("11name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = g1.getProfile()
                                profile.displayName = string
                                g1.updateProfile(profile)
                                g1.sendMessage(msg.to,"Nama diganti jadi " + string + "")
#TAGALL
                        elif msg.text.lower().startswith("mention"):
                          if msg._from in admin:						
                            data = msg.text[len("mention"):].strip()
                            if data == "":
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    akh = akh + len(str(count)) + 2 + 5
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                            elif data[0] == "<":
                                mentargs = int(data[1:].strip())
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    if count > mentargs:
                                                break
                                    akh = akh + len(str(count)) + 2 + 5
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                            elif data[0] == ">":
                                mentargs = int(data[1:].strip())
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                if mentargs >= 0:
                                    strt = len(str(mentargs)) + 2
                                else:
                                    strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    if count < mentargs:
                                                count += 1
                                                continue
                                    akh = akh + len(str(count)) + 2 + 5
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                            elif data[0] == "=":
                                mentargs = int(data[1:].strip())
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    if count != mentargs:
                                                count += 1
                                                continue
                                    akh = akh + len(str(count)) + 2 + 5
                                    strt = len(str(count)) + 2
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendReplyMessage(msg_id, to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")

                        elif cmd == "tag":
                          if msg._from in admin:
                            try:group = aditmadzs.getGroup(to);midMembers = [contact.mid for contact in group.members]
                            except:group = aditmadzs.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                            midSelect = len(midMembers)//20
                            for mentionMembers in range(midSelect+1):
                                no = 0
                                ret_ = "╭───「 Mention Members 」"
                                dataMid = []
                                if msg.toType == 2:
                                    for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                        dataMid.append(dataMention.mid)
                                        no += 1
                                        ret_ += "\n"+"├≽ {}. @!".format(str(no))
                                    ret_ += "\n╰───「 Total {} Members 」".format(str(len(dataMid)))
                                    aditmadzs.sendReplyMention(msg_id, to, ret_, dataMid)
                                else:
                                    for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                        dataMid.append(dataMention.mid)
                                        no += 1
                                        ret_ += "\n"+"├≽ {}. @!".format(str(no))
                                    ret_ += "\n╰───「 Total {} Members 」".format(str(len(dataMid)))
                                    aditmadzs.sendReplyMention(msg_id, to, ret_, dataMid)
#LIST
                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"╭───「 List bot 」\n\n"+ma+"\n╰───「 Total %s bot 」" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"• Admin Bot\n\n• Creator:\n"+ma+"\n• Admin:\n"+mb+"\n• Staff:\n"+mc+"\n• Total「%s」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +aditmadzs.getGroup(group).name + "\n"    
                                gid = protectantijs
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +aditmadzs.getGroup(group).name + "\n"                                
                                aditmadzs.sendMessage(msg.to,"╭───「 List protection 」\n├≽ PROTECT URL :\n"+ma+"\n├≽ PROTECT KICK :\n"+mb+"\n├≽ PROTECT JOIN :\n"+md+"\n├≽ PROTECT CANCEL:\n"+mc+"\n├≽ PROTECT INVITE :\n"+me+"\n├≽ PROTECT ANTIJS :\n"+mf+"\n╰───「 Total %s Protect yang aktif 」" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite)+len(protectantijs))))
#RESPONNAME
                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sendMention1(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 1 ", "")
                                sendMention2(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 2 ", "")
                                sendMention3(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 3 ", "")
                                sendMention4(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 4 ", "")
                                sendMention5(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 5 ", "")
                                sendMention6(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 6 ", "")
                                sendMention7(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 7 ", "")
                                sendMention8(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 8 ", "")
                                sendMention9(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 9 ", "")
                                sendMention10(msg.to, sender, "「ＳＥＬＦＢＯＴＢＹＭＡＸ」 10 ", "")

                        elif cmd == "name":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                k1.sendMessage(msg.to,responsename1, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})
                                k2.sendMessage(msg.to,responsename2, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})
                                k3.sendMessage(msg.to,responsename3, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})
                                k4.sendMessage(msg.to,responsename4, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})
                                k5.sendMessage(msg.to,responsename5, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})
                                k6.sendMessage(msg.to,responsename6, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})
                                k7.sendMessage(msg.to,responsename7, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})
                                k8.sendMessage(msg.to,responsename8, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})
                                k9.sendMessage(msg.to,responsename9, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})
                                k10.sendMessage(msg.to,responsename10, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CHECKBOT', 'AGENT_LINK': 'http://line.me/ti/p/~max.self'})					
#INVITE BOT
                        elif cmd == "inv":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID]
                                    aditmadzs.inviteIntoGroup(msg.to, anggota)
                                    k1.acceptGroupInvitation(msg.to)
                                    k2.acceptGroupInvitation(msg.to)
                                    k3.acceptGroupInvitation(msg.to)
                                    k4.acceptGroupInvitation(msg.to)								
                                    k5.acceptGroupInvitation(msg.to)
                                    k6.acceptGroupInvitation(msg.to)
                                    k7.acceptGroupInvitation(msg.to)
                                    k8.acceptGroupInvitation(msg.to)
                                    k9.acceptGroupInvitation(msg.to)
                                    k10.acceptGroupInvitation(msg.to)
                                except:
                                    pass
#INVITE PROTECT JS
                        elif cmd == "pro js":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = aditmadzs.getGroup(msg.to)
                                    aditmadzs.inviteIntoGroup(msg.to, [g1MID])
                                    aditmadzs.sendMessage(msg.to,"Grup「 "+str(ginfo.name)+" 」Adit Dari JS")
                                except:
                                    pass
#JOIN BYE
                        elif cmd == "in":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k5.acceptGroupInvitationByTicket(msg.to,Ticket)	
                                k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k10.acceptGroupInvitationByTicket(msg.to,Ticket)	
                                G = k10.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k10.updateGroup(G)

                        elif cmd == "out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                sendMention1(msg.to, sender, "Selamat tinggal, teman kita dulu.\n", " !")
                                k1.leaveGroup(msg.to)
                                k2.leaveGroup(msg.to)
                                k3.leaveGroup(msg.to)
                                k4.leaveGroup(msg.to)
                                k5.leaveGroup(msg.to)								
                                k6.leaveGroup(msg.to)
                                k7.leaveGroup(msg.to)
                                k8.leaveGroup(msg.to)
                                k9.leaveGroup(msg.to)
                                k10.leaveGroup(msg.to)

                        elif cmd == "g in":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = g1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                g1.updateGroup(G)

                        elif cmd == "g1 in":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = g1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                g1.updateGroup(G)

                        elif cmd == "g bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                g1.leaveGroup(msg.to)

                        elif cmd == "g1 bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                g1.leaveGroup(msg.to)

                        elif cmd == "outall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    k1.leaveGroup(i)
                                    k2.leaveGroup(i)
                                    k3.leaveGroup(i)
                                    k4.leaveGroup(i)
                                    k5.leaveGroup(i)
                                    k6.leaveGroup(i)
                                    k7.leaveGroup(i)
                                    k8.leaveGroup(i)
                                    k9.leaveGroup(i)
                                    k10.leaveGroup(i)
#SPEED BOT
                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = aditmadzs.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = aditmadzs.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = aditmadzs.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                aditmadzs.sendMessage(msg.to, "• Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:                              
                               aditmadzs.sendMessage(msg.to, "Checking speed...")
                               start = time.time() 
                               time.sleep(0.007)
                               elapsed_time = time.time() - start
                               aditmadzs.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
       
                        elif cmd == "speedbot" or cmd == "spb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sendMention1(msg.to, sender, "Checking speed... \n", "")
                               start = time.time() 
                               time.sleep(0.007)  
                               elapsed_time = time.time() - start
                               k1.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.007)  
                               elapsed_time = time.time() - start
                               k2.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.007)  
                               elapsed_time = time.time() - start
                               k3.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.007)  
                               elapsed_time = time.time() - start
                               k4.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.007)  
                               elapsed_time = time.time() - start
                               k5.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.007)  
                               elapsed_time = time.time() - start
                               k6.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.007)  
                               elapsed_time = time.time() - start
                               k7.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.007) 
                               elapsed_time = time.time() - start
                               k8.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.007)  
                               elapsed_time = time.time() - start
                               k9.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
                               start = time.time() 
                               time.sleep(0.007)  
                               elapsed_time = time.time() - start
                               k10.sendMessage(msg.to, "Speed sending message took\n{} detik".format(str(elapsed_time)))
#READ
                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['MAXreadPoint'][msg.to] = msg_id
                                 Setmain['MAXreadMember'][msg.to] = {}
                                 aditmadzs.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['MAXreadPoint'][msg.to]
                                 del Setmain['MAXreadMember'][msg.to]
                                 aditmadzs.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['MAXreadPoint']:
                                if Setmain['MAXreadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['MAXreadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "「 Result {} member 」\n\n「 Lurkers 」\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "「 {} 」".format(str(aditmadzs.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        aditmadzs.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['MAXreadPoint'][msg.to]
                                        del Setmain['MAXreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['MAXreadPoint'][msg.to] = msg.id
                                    Setmain['MAXreadMember'][msg.to] = {}
                                else:
                                    aditmadzs.sendMessage(msg.to, "User kosong...")
                            else:
                                aditmadzs.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  aditmadzs.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  aditmadzs.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  aditmadzs.sendMessage(msg.to, "Sudak tidak aktif")
#SPAM
                        elif cmd.startswith('spamtag '):
                          if sender in admin:
                            sep = text.split(" ")
                            num = int(sep[1])                           
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    for var in range(0,num):
                                        aditmadzs.sendMention(to, "@!", [ls])

                        elif cmd.startswith("spamchat"):
                          if sender in admin:
                            text = text.split(" ")
                            jmlh = int(text[2])
                            balon = jmlh * (text[3]+"\n")
                            if text[1] == "on":
                                if jmlh <= 1000:
                                    for x in range(jmlh):
                                        aditmadzs.sendMessage(to, text[3])
                                else:
                                    aditmadzs.sendMessage(msg.to, "Sorry the amount is too much :)")
                            elif text[1] == "off":
                              if jmlh <= 1000:
                                aditmadzs.sendMessage(to, balon)
                              else:
                                aditmadzs.sendMessage(msg.to,"Sorry the amount is too much :)")
                   
                        elif cmd.startswith('spamcallto '):
                          if msg._from in admin:
                            sep = text.split(" ")
                            num = int(sep[1])
                            try:                           
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            group = aditmadzs.getGroup(to)
                                            members = [ls]
                                            kunkun = aditmadzs.getContact("ud134cbd020e975960892558a13aa6dba").displayName
                                            aditmadzs.acquireGroupCallRoute(to)
                                            aditmadzs.inviteIntoGroupCall(to, contactIds=members)
                                        aditmadzs.sendMention(to, "Succesfully Spamcall to @!", [ls])
                            except Exception as error:
                                aditmadzs.sendMessage(to, str(error))
  
                        elif cmd.startswith('spamcall '):
                          if msg._from in admin:
                            if msg.toType == 2:
                                sep = text.split(" ")
                                strnum = text.replace(sep[0] + " ","")
                                num = int(strnum)
                                aditmadzs.sendMessage(to, "Succesfully Spam Call to Group")
                                for var in range(0,num):
                                   group = aditmadzs.getGroup(to)
                                   members = [mem.mid for mem in group.members]
                                   aditmadzs.acquireGroupCallRoute(to)
                                   aditmadzs.inviteIntoGroupCall(to, contactIds=members)

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, str(Setmain["MAXmessage1"]))

                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
#PROTECTSION
                        elif 'Prourl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Prourl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr[msg.to] = True
                                       f=codecs.open('protectqr.json','w','utf-8')
                                       json.dump(protectqr, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         del protectqr[msg.to]
                                         f=codecs.open('protectqr.json','w','utf-8')
                                         json.dump(protectqr, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Prokick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Prokick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Prokick1 ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Prokick1 ','')
                              if spl == 'on':
                                  if msg.to in protectkick1:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick1.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect kick 1 diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick1:
                                         protectkick1.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect kick 1 dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick 1 sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Projoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Projoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Proinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Proinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                                      

                        elif 'Antijs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Pro Antijs sudah aktif"
                                  else:
                                       protectantijs[msg.to] = True
                                       f=codecs.open('protectantijs.json','w','utf-8')
                                       json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Pro Antijs diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         del protectantijs[msg.to]
                                         f=codecs.open('protectantijs.json','w','utf-8')
                                         json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)												 
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Pro JS dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Pro JS sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Ghost diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Ghost dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                 

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
#KICK OUT
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = aditmadzs.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           aditmadzs.updateGroup(G)
                                           invsend = 0
                                           Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                           g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           g1.kickoutFromGroup(msg.to, [target])
                                           g1.leaveGroup(msg.to)
                                           X = aditmadzs.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           aditmadzs.updateGroup(X)
                                       except:
                                           pass
          
                        elif ("Kick " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           protectqr[msg.to] = True
                                           f=codecs.open('protectqr.json','w','utf-8')
                                           json.dump(protectqr, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif text.lower() in ['kickban','killban']:
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                gMembMids = [contact.mid for contact in group.members]
                                matched_list = []
                            for tag in wait["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                aditmadzs.sendMessage(msg.to,"There was no blacklist user")
                                return
                            for jj in matched_list:
                                aditmadzs.kickoutFromGroup(msg.to,[jj])
                            aditmadzs.sendMessage(msg.to,"Blacklist kicked out")

                        elif ("Vk " in msg.text):
                          if msg._from in admin:
                            if msg.toType == 2:
                                prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                                for i in range(len(prov)):
                                    aditmadzs.kickoutFromGroup(msg.to,[prov[i]["M"]])

                        elif ("Bk " in msg.text):
                          if msg._from in admin:
                            if msg.toType == 2:
                                prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                                for i in range(len(prov)):
                                    random.choice(ABC).kickoutFromGroup(msg.to,[prov[i]["M"]])
                                           
                        elif ("maxkick" in msg.text):
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("maxkick","")                                 
                                 gs = k1.getGroup(msg.to)
                                 gs = k2.getGroup(msg.to)
                                 gs = k3.getGroup(msg.to)
                                 gs = k4.getGroup(msg.to)
                                 gs = k5.getGroup(msg.to)
                                 gs = k6.getGroup(msg.to)
                                 gs = k7.getGroup(msg.to)
                                 gs = k8.getGroup(msg.to)
                                 gs = k9.getGroup(msg.to)
                                 gs = k10.getGroup(msg.to)
                                 aditmadzs.sendMessage(msg.to,"「 Papay Sayang 」")
                                 aditmadzs.sendMessage(msg.to,"「 Sorry r̸o̸o̸m̸ n̸y̸a̸ k̸a̸m̸i̸ s̸i̸t̸a̸ s̸e̸e̸ y̸o̸u̸ s̸l̸a̸m̸ d̸a̸r̸i̸ 」")
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     aditmadzs.sendMessage(msg.to,"ʙᴏᴛs ʟɪᴍɪᴛ")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                             if not target in staff:
                                               try:
                                                   maxkick= [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]
                                                   kicker=random.choice(maxkick)
                                                   kicker.kickoutFromGroup(msg.to,[target])
                                                   print (msg.to,[g.mid])
                                               except Exception as error:
                                                   aditmadzs.sendMessage(msg.to, str(error))

                        elif text.lower() == 'maxkill':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                           	if msg.toType == 2:
                                  ginfo = aditmadzs.getGroup(msg.to)
                                  aditmadzs.sendMessage(msg.to, "Proses Cleanse....")
                                  aditmadzs.sendMessage(msg.to, "silentkiller \nmember : " +str(len(ginfo.members)) + " \nFuck you...")
                                  G = aditmadzs.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  aditmadzs.updateGroup(G)
                                  Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                  k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  _name = text.lower().replace('maxkill','')
                                  gs = k1.getGroup(msg.to)
                                  gs = k2.getGroup(msg.to)
                                  gs = k3.getGroup(msg.to)
                                  gs = k4.getGroup(msg.to)
                                  gs = k5.getGroup(msg.to)
                                  gs = k6.getGroup(msg.to)
                                  gs = k7.getGroup(msg.to)
                                  gs = k8.getGroup(msg.to)
                                  gs = k9.getGroup(msg.to)
                                  gs = k10.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                  	if _name in g.displayName:
                                  	   targets.append(g.mid)
                                  if targets == []:
                                  	aditmadzs.sendMessage(msg.to, "ʙᴏᴛs ʟɪᴍɪᴛᴇ")
                                  else:
                                       for target in targets:
                                        if not target in Bots:
                                           if not target in admin:
                                              if not target in staff:
                                                 try:
                                                      random.choice(ABC).kickoutFromGroup(msg.to,[target])
                                                      G = aditmadzs.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      aditmadzs.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      aditmadzs.updateGroup(G)
                                                 except:
                                                      pass
#ADMIN ADD
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           staff.remove(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Aditmadzs:
                                       try:
                                           Bots.remove(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:delete" or text.lower() == 'admin:delete':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:delete" or text.lower() == 'staff:delete':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:delete" or text.lower() == 'bot:delete':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                aditmadzs.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "cek admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = k1.getContact(i)
                                    k1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cek staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = k1.getContact(i)
                                    k1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cek bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = k1.getContact(i)
                                    k1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
#COMMAND ON OFF
                        elif cmd == "mentionkick on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                aditmadzs.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "mentionkick off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                aditmadzs.sendMessage(msg.to,"Notag dinonaktifkan")
                                
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                aditmadzs.sendMessage(msg.to, "「 Status Invite 」\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                aditmadzs.sendMessage(msg.to, "「 Status Invite 」\nInvite via contact dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                aditmadzs.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                aditmadzs.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                aditmadzs.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                aditmadzs.sendMessage(msg.to,"Auto respon dinonaktifkan")
                                
                        elif cmd == "gift on" or text.lower() == 'respongift on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                aditmadzs.sendMessage(msg.to,"Auto respon gift diaktifkan")

                        elif cmd == "gift off" or text.lower() == 'respongift off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                aditmadzs.sendMessage(msg.to,"Auto respon gift dinonaktifkan")                                

                        elif cmd == "join on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                aditmadzs.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "join off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                aditmadzs.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "join1 on" or text.lower() == 'autojoin1 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin1"] = True
                                aditmadzs.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "join1 off" or text.lower() == 'autojoin1 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin1"] = False
                                aditmadzs.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "leave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "leave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "leave1 on" or text.lower() == 'autoleave1 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave1"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Leave Diaktifkan")

                        elif cmd == "leave1 off" or text.lower() == 'autoleave1 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave1"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Leave Dimatikan")

                        elif cmd == "block on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                aditmadzs.sendMessage(msg.to,"Auto block diaktifkan")

                        elif cmd == "block off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                aditmadzs.sendMessage(msg.to,"Auto block dinonaktifkan")

                        elif cmd == "add on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Add Diaktifkan")

                        elif cmd == "add off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Add Dimatikan")

                        elif cmd == "read on" or text.lower() == 'read on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                aditmadzs.sendMessage(msg.to,"Deteksi read diaktifkan")

                        elif cmd == "read off" or text.lower() == 'read off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                aditmadzs.sendMessage(msg.to,"Deteksi read dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                aditmadzs.sendMessage(msg.to,"Detect Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                aditmadzs.sendMessage(msg.to,"Detect Sticker Dimatikan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                aditmadzs.sendMessage(msg.to,"Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                aditmadzs.sendMessage(msg.to,"Auto Join Ticket Dimatikan")
#BLACKLIST
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bl" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendReplyWithFooter(msg.to,"• Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"• Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "bc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = aditmadzs.getContact(i)
                                        aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                                        
                        elif cmd == "cb" or text.lower() == 'cbl':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                              aditmadzs.sendMessage(msg.to,"Succes Bersihkan「 {} 」Daftar Blacklist".format(str(len(wait["blacklist"]))))
                              wait["blacklist"] = {}
#SET MESSAGE
                        elif cmd.startswith("set autoadd: "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            try:
                                wait["autoAddMessage"] = txt
                                aditmadzs.sendReplyMessage(msg.to, "Berhasil mengubah pesan auto add menjadi : 「{}」".format(txt))
                            except:
                                aditmadzs.sendReplyMessage(msg.to, "Gagal mengubah pesan auto add")

                        elif cmd.startswith("set autoblock: "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            try:
                                wait["autoBlockMessage"] = txt
                                aditmadzs.sendReplyMessage(msg.to, "Berhasil mengubah pesan auto block menjadi : 「{}」".format(txt))
                            except:
                                aditmadzs.sendReplyMessage(msg.to, "Gagal mengubah pesan auto block")

                        elif cmd.startswith("set autojoin: "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            try:
                                wait["autoJoinMessage"] = txt
                                aditmadzs.sendReplyMessage(msg.to, "Berhasil mengubah pesan auto join menjadi : 「{}」".format(txt))
                            except:
                                aditmadzs.sendReplyMessage(msg.to, "Gagal mengubah pesan auto join")
                                    
                        elif cmd.startswith("set member: "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            txt = int(sep[1])
                            try:
                                wait["memberCancel"]["members"] = txt
                                aditmadzs.sendReplyMessage(msg.to, "Succesfully set auto join group if mem {}".format(txt))
                            except:
                                aditmadzs.sendReplyMessage(msg.to, "Gagal mengubah auto join group")

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Leave Msg」\nLeave Message diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Respon Msg」\nRespon Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["MAXmessage1"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Spam Msg」\nSpam Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Sider Msg」\nSider Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Welcome Msg」\nWelcome Message lu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Leave Msg」\nLeave Message lu :\n\n「 " + str(wait["leave"]) + " 」")                                 

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Respon Msg」\nRespon Message lu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Spam Msg」\nSpam Message lu :\n\n「 " + str(Setmain["ADITMADZSmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Sider Msg」\nSider Message lu :\n\n「 " + str(wait["mention"]) + " 」")
#JOINTICKET
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = aditmadzs.findGroupByTicket(ticket_id)
                                     aditmadzs.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     group1 = k1.findGroupByTicket(ticket_id)
                                     k1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = k2.findGroupByTicket(ticket_id)
                                     k2.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = k3.findGroupByTicket(ticket_id)
                                     k3.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = k4.findGroupByTicket(ticket_id)
                                     k4.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = k5.findGroupByTicket(ticket_id)
                                     k5.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = k6.findGroupByTicket(ticket_id)
                                     k6.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = k7.findGroupByTicket(ticket_id)
                                     k7.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = k8.findGroupByTicket(ticket_id)
                                     k8.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = k9.findGroupByTicket(ticket_id)
                                     k9.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = k10.findGroupByTicket(ticket_id)
                                     k10.acceptGroupInvitationByTicket(group1.id,ticket_id)
#END
    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
