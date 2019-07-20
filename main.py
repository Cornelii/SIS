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
    'COUNTRIES3': 0,
    'TOWER': 0,
    'WINDBREAKER': 0,
    'COOKGO': 0,
    'JAMESONHILL': 0,
    'PINK': 0,
    'MAGICSCROLL': 0,
    'KILLERFOODS': 0,
    'SPERMAN': 0
    }

if __name__ == '__main__':
    print(toon)
    print(new)

    for Toon in toon_list:
        sis = SIS(title=Toon.title)
        sis.scrap_pages(Toon, toon[Toon.title], new[Toon.title])
