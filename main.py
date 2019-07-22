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
LAID = NWToon('LAID', 729039, 'mon')
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
    'COUNTRIES3': 124,
    'TOWER': 439,
    'WINDBREAKER': 268,
    'COOKGO': 58,
    'JAMESONHILL': 184,
    'PINK': 49,
    'MAGICSCROLL': 198,
    'KILLERFOODS': 34,
    'SPERMAN': 4,
    'LAID': 6,
    }

if __name__ == '__main__':
    print(toon)
    print(new)

    for Toon in toon_list:
        sis = SIS(title=Toon.title)
        if toon[Toon.title] == new[Toon.title]:
            pass
        elif toon[Toon.title] != 0:
            sis.scrap_pages(Toon, toon[Toon.title]+1, new[Toon.title])
        else:
            sis.scrap_pages(Toon, 1, new[Toon.title])

    # update latest.txt
    with open('latest.txt', 'w') as f:
        for Toon in toon_list:
            f.write(f"{Toon.title} {new[Toon.title]}\n")
