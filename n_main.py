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
    'COUNTRIES3': 161,
    'TOWER': 457,
    'WINDBREAKER': 286,
    'COOKGO': 76,
    'JAMESONHILL': 203,
    'PINK': 67,
    'MAGICSCROLL': 217,
    'KILLERFOODS': 53,
    'SPERMAN': 23,
    'JANGBODYGUARD': 28,
    'DOCTORNDOCTOR': 28,
    'MANMULL': 22,
    }

# Toon Model => Toon을 상속하고, self.url_generator = generator 시키는 제너레이터 레퍼 펑션 generate_url 상속

def isValid(dic1, dic2, title):
    if (dic1.get(title) and dic2.get(title)):
        return True
    else: 
        return False

if __name__ == '__main__':
    #Toon = n_toon_list[0]
    #sis = SIS()

    #Toon.generate_url(47, 50)
    #sis.set_title(Toon.title)
    #sis.scrap_pages(Toon)

    cookie = "NNB=2AE7WJDTY3DF2; nx_ssl=2; _ga=GA1.2.1470064561.1574518769; ASID=da949dfb0000016eba68b3f700000068; nid_inf=1170093397; NID_AUT=TmHINFT/HpohJ+qMRAgA82Ce0hrQyZPFmlUFxLOJEcSSKxWEsamYKma+nSqhUOSR; NID_SES=AAABshQd3kQQijZZk+bYgf5IjAT3NsYD7ELINdSqg2hqyWYhgaB+WKAmnYhHCSrCBiSe4NBcsEZj8xvjJwdzA24tM7X33UrSNHb8e5YqKGNdp4IMdzQ+Sv7w8IMG4hniIwvhxuODSLyyTQ113bsEWRDWj2PgTYtZL/KXBdybVdDc5Ab/TUtzqNu3bwzCzOBikbxNe/tIvpaD1n8lqHaD1y3KYeBbDy+aq4sR/e+qcpXASZXJ9Vq/q78VnnO69YVlcu+XAdyLj2iu9eXQCzUfFoOns8nB1rK2gPX9UDyzMDqoxI0rBG7MnpeQaoQYvGPzPbcw8B+RacnUMABY+lhsv747SNckXPOUcwONwfdTJs4UOU3QTQoMscMOwlj2ST3PhwdP2XSkV9BPBOvWMRj+xgQfK8woMKojIkm0lLOHypx8+mjvVgQXQc1EI2WHraoCd7QyvS6lNRvQbkgVOGuEKyd7MFzHKEugBDJhYBTIT+As39gfctW700a/uLepHerwZG8hkE51iOVcZxxNRv6pCbFdKB8QWpGphbKRbhr4dHVuFP90yFhKNCh2d3YMQ1P748/r6uxA01WK+scJmB4JvfensuU=; NID_JKL=BFmAkEtLSkAuM0J+HeZFlN/DWhWIvRBkJHgxhHg+FkI=; JSESSIONID=8636BABE034E21D6FB6C6A780B91246A"
    sis = SIS()
    sis.page_loader.set_cookies(cookie)

    latest = {}
    with open('latest.txt','r') as f:
        for line in f:
            a = line.strip().split()
            latest[a[0]] = int(a[1])

    for toon in n_toon_list:
        if isValid(new, latest, toon.title):
            new_episode = new[toon.title]
            latest_episode = latest[toon.title]
            toon.generate_url(latest_episode+1, new_episode)
            sis.set_title(toon.title)
            sis.scrap_pages(toon)
        
    with open('latest.txt', 'w') as f:
        for key, value in new.items():
            f.write(f"{key} {value}")
