

class WebToon:
    def __init__(self, title, Id, weekday):
        self.title = title
        self.id = Id
        self.weekday = weekday

class NWToon(WebToon):
    def __init__(self, title, Id, weekday, rate=0):
        super().__init__(title, Id, weekday)
        self.url = f'https://comic.naver.com/webtoon/detail.nhn?titleId={self.id}&weekday={self.weekday}&no='
        self.rate = rate

    def page_url(self, no=1):
        return self.url+str(no)



COUNTRIES3 = NWToon('COUNTRIES3', 711422, 'tue')
TOWER = NWToon('TOWER', 183559, 'mon')
WINDBREAKER = NWToon('WINDBREAKER', 602910, 'mon')
COOKGO = NWToon('COOKGO', 703849, 'mon')
JAMESONHILL = NWToon('JAMESONHILL', 671421, 'wed')
PINK = NWToon('PINK', 715159, 'sat')
MAGICSCROLL = NWToon('MAGICSCROLL', 655746, 'sun')
KILLERFOODS = NWToon('KILLERFOODS', 720117, 'sun')
SPERMAN = NWToon('SPERMAN', 730259, 'sun', 18)
JANGBODYGUARD=NWToon("JANGBODYGUARD",728750,'mon')
DOCTORNDOCTOR=NWToon("DOCTORNDOCTOR",732955,'sun')
MANMULL=NWToon("MANMULL", 729964, 'thu')


toon_list = [COUNTRIES3, TOWER, WINDBREAKER, COOKGO, JAMESONHILL, PINK, MAGICSCROLL, KILLERFOODS, SPERMAN, JANGBODYGUARD,DOCTORNDOCTOR, MANMULL]
