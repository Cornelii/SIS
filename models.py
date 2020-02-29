from utils import PageLoader

# ToonModel 을 Json Serializable하게 구성하고 JSON으로 version 관리
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

    ## Decorator 방식으로 변경해보기
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
SPERMAN = NWToon('SPERMAN', 730259, 'sun', 18)
JANGBODYGUARD=NWToon("JANGBODYGUARD", 728750,'mon')
DOCTORNDOCTOR=NWToon("DOCTORNDOCTOR", 732955,'sun')
MANMULL=NWToon("MANMULL", 729964, 'thu')

n_toon_list = [COUNTRIES3, TOWER, WINDBREAKER, COOKGO, JAMESONHILL,
                PINK, MAGICSCROLL, SPERMAN, JANGBODYGUARD,
                DOCTORNDOCTOR, MANMULL]


class IGToon(Toon):

    def __init__(self, title, list_url, parse_str=".post-wrapper p a", base_url="https://eguru.tumblr.com", version_size=300):
        super().__init__(title, version_size)
        self.list_url = list_url
        self.parse_str = parse_str
        self.base_url = base_url
        self.rate = 0

    def generate_url(self):
        PL = PageLoader()
        urls = PL.get_list(self.list_url, self.parse_str)

        def generator():
            for url in urls:
                yield url["href"][-47:], self.base_url + url["href"]

        self.url_generator = generator


SLAMDUNK = IGToon("Slam Dunk", "https://eguru.tumblr.com/%EC%8A%AC%EB%9E%A8%EB%8D%A9%ED%81%AC")
NARUTO = IGToon("Naruto", "https://eguru.tumblr.com/%EB%82%98%EB%A3%A8%ED%86%A0")
ONEPIECE = IGToon("ONEPIECE", "https://eguru.tumblr.com/one-piece")



