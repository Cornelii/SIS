
class Toon:
    def __init__(self, title, version_size=300):
        self.title = title
        self.url_generator = None
        self.version = [0]*version_size

    def generate_url(self):
        raise NotImplementedError


## N Models
class NWToon(Toon):
    def __init__(self, title, Id, weekday, rate=0, version_size=300):
        super().__init__(title, version_size)
        self.id = Id
        self.rate = rate
        self.weekday = weekday
        self.url = f'https://comic.naver.com/webtoon/detail.nhn?titleId={self.id}&weekday={self.weekday}&no='

    def page_url(self, no=1):
        return self.url+str(no)

    def generate_url(self, start, end):
        def generator():
            for i in range(start, end+1):
                url = self.page_url(i)
                yield i, url
        self.url_generator = generator


COUNTRIES3 = NWToon('COUNTRIES3', 711422, 'tue')
TOWER = NWToon('TOWER', 183559, 'mon')
WINDBREAKER = NWToon('WINDBREAKER', 602910, 'mon')
COOKGO = NWToon('COOKGO', 703849, 'mon')
JAMESONHILL = NWToon('JAMESONHILL', 671421, 'wed')
PINK = NWToon('PINK', 715159, 'sat')
MAGICSCROLL = NWToon('MAGICSCROLL', 655746, 'sun')
KILLERFOODS = NWToon('KILLERFOODS', 720117, 'sun')
SPERMAN = NWToon('SPERMAN', 730259, 'sun', 18)
JANGBODYGUARD=NWToon("JANGBODYGUARD", 728750,'mon')
DOCTORNDOCTOR=NWToon("DOCTORNDOCTOR", 732955,'sun')
MANMULL=NWToon("MANMULL", 729964, 'thu')

n_toon_list = [COUNTRIES3, TOWER, WINDBREAKER, COOKGO, JAMESONHILL,
                PINK, MAGICSCROLL, KILLERFOODS, SPERMAN, JANGBODYGUARD,
                DOCTORNDOCTOR, MANMULL]

