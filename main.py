import sys
from utils import SIS
from models import *

'''
COUNTRIES3 = NWToon(711422, 'tue')
TOWER = NWToon(183559, 'mon')
WINDBREAKER = NWToon(602910, 'mon')
COOKGO = NWToon(703849, 'mon')
JAMESONHILL = NWToon(671421, 'wed')
PINK = NWToon(715159, 'sat')
MAGICSCROLL = NWToon(655746, 'sun')
KILLERFOODS = NWToon(720117, 'sun')
SPERMAN = NWToon(730259, 'sun')
MANMULL=NWToon("MANMULL", 729964, 'thu')
GUARD=NWToon("JANGBODYGUARD",728750,'mon')
DOCTORNDOCTOR=NWToon("DOCTORNDOCTOR",732955,'sun')
'''

sys.stdin = open('latest.txt', 'r')
toon = {}
while True:
    try:
        name, ed = input().split()
        toon[name] = int(ed)
    except:
        break

new = {
    'COUNTRIES3': 155,
    'TOWER': 454,
    'WINDBREAKER': 283,
    'COOKGO': 73,
    'JAMESONHILL': 200,
    'PINK': 64,
    'MAGICSCROLL': 213,
    'KILLERFOODS': 49,
    'SPERMAN': 19,
    'JANGBODYGUARD': 25,
    'DOCTORNDOCTOR': 11,
    'MANMULL': 19,
    }

if __name__ == '__main__':
    print(toon)
    print(new)
    cookie ="NNB=WY6EUAV6FKVV2; nx_ssl=2; ASID=0e25eebf0000016de4cfe9c800000053; nid_inf=1133345442; NID_AUT=WDhpbggOAqyEO+vgZe0/ToPkjsf8JtjFotAeDXJQ4gz0WIO1ZWUQDimzrFr/Ntcn; NID_SES=AAABs/xHrXrGQ/71N4jPuyEj9OD8VDahgWXzHf3tbfeqez+oewN+VzFXMV8YAtPOEMSe2NEAHcNnYfYbWoeccRxBf4llEINUyiaQ+xacjdagcpSmbhubY7ZlF2+SSHOOQLva+u2n3ZnzszUolSjN85fDKVlDmub/hglaqeVXmRtenvkrH3L5XPkn6iOXWHPoaS7Ug4G5POxpcBu5wsnbx+x65wVRJjRgJ8LXmZ8q7Mfpa6gl75hTnFx7lIXq3fgcqW5HTs6z+G5bef78Bgs9no9WQmHxFU9ZMSNBVfiaA8RbJHNsDc0TCbmetAYcfArtQvDhuLd+0xvG9ttUKavb3fmgiMScQwMplnKqEUaFjlakQfizDvxuiJ/u8pMMSTLboyt1nuY/tGY7F2P9x5ma/z8z7AjjSAmKg2qJ7hNsI33lSv6KhHmE5UONlWXTjpZEEcQdITsZtsaQQrlI5F+9HqNhEi9MKJuoL023xyNBvtxj2FgqDpOesEg9/qoauvgvw4wh7ivmbThJEp9yrSWZ1XeAg5KhHkx8sbgouXsPvhpmgBRaOZ/2hDljnbsYOetnIhO0VUb5e/vVaavEXCb87A7AtVM=; NID_JKL=MIjx6IcdHB8OUR84wchqIAWTQhG3gm+JlML4QJfogRk=; JSESSIONID=013CEDC5AA19A9A2F8FF07242A1647E5"
    # cookie = 

    for Toon in toon_list:
        sis = SIS(title=Toon.title)
        if toon[Toon.title] == new[Toon.title]:
            pass
        elif toon[Toon.title] != 0:
            sis.scrap_pages(Toon, toon[Toon.title]+1, new[Toon.title], cookie=cookie)
        else:
            sis.scrap_pages(Toon, 1, new[Toon.title], cookie=cookie)

    # update latest.txt
    with open('latest.txt', 'w') as f:
        for Toon in toon_list:
            f.write(f"{Toon.title} {new[Toon.title]}\n")
