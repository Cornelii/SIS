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
    'COUNTRIES3': 144,
    'TOWER': 449,
    'WINDBREAKER': 278,
    'COOKGO': 68,
    'JAMESONHILL': 195,
    'PINK': 58,
    'MAGICSCROLL': 208,
    'KILLERFOODS': 44,
    'SPERMAN': 14,
    'JANGBODYGUARD': 20,
    'DOCTORNDOCTOR': 11,
    'MANMULL': 14,
    }

if __name__ == '__main__':
    print(toon)
    print(new)
    cookie ="NNB=2WI6OOJLEOIF2; nx_ssl=2; nid_inf=1085230822; NID_AUT=2Wg7tzA8SoYkSZ5C10H2nv/sPgSKKqp+dM2LIhUIyhQq/RxbkjcDszAlSJbeTsRB; NID_SES=AAABskCnayGXn2gAIjARLvHgGU1bpi5O4dA+D6gZQYPdWZCw7yXLxBrDUUcbXmBXMGOeDXY+Qwm22IPMmHhTyz6ZXjPB+UvRpzgaxIw7H6c3LGmegrFzNnEByVrFNwmsj8+pfggdnPEanQSjBlAXWNFzlfmUsx+wvRM4p7D09w6hE7Nf0h8ImcRv4lQZa0iQHIstnFVCzP3vKzbNuG317PEtGrReJf/oSobyZDMhUx7LdtZRJ6tPv0oLK4/arvJrL83Udj7XN5bP7uHmkTfKToG9pP+XxhlfRbndsNIMwgx8ypiC22+hz9HupXtz0wp086pkB0Dp1MNnlgXpSATsfetUG3Pnm54qrtrOFRfCTrqWnocnRiUtX3m0RAZljYQU8E4fQtZLPLj5b+Bb9uxy1KoxCRUvPgl9y3mOJSJqE2wbLZ5N6351NH3r18uqI4+bbobHe84P4pPKw9/du/S+pFUFPfBJ+aKztfzDOQNHi4rcazAtqNU9q6AgQaEnPBdIZ3Aw9kcLBhzrlXReIDuA5WntE80grBdblnj4wqemTVOTvw2UdepiijHb0FEXIeRVACKWo1osGpxFUr0ILtxNb7pjLCU=; NID_JKL=x4HxnbioRl1Jlay5NoqNLp1IIFowDgC5bRO+B6ncz3Q=; increase=""; JSESSIONID=31DA047B0F69BB36C3478B1320DB5C84"
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
