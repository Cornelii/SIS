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

# Toon Model => Toon을 상속하고, self.url_generator = generator 시키는 제너레이터 레퍼 펑션 generate_url 상속

if __name__ == '__main__':
    Toon = n_toon_list[0]
    sis = SIS()

    Toon.generate_url(47, 50)
    sis.set_title(Toon.title)
    sis.scrap_pages(Toon)

