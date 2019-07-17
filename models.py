

class WebToon:
    def __init__(self, id, weekday):
        self.id = id
        self.weekday = weekday

class NWToon(WebToon):
    def __init__(self, id, weekday):
        super().__init__(id, weekday)
        self.url = f'https://comic.naver.com/webtoon/detail.nhn?titleId={self.id}&weekday={self.weekday}&no='

    def page_url(self, no=1):
        return self.url+str(no)


CONTRIES3 = NWToon(711422, 'tue')
TOWER = NWToon(183559, 'mon')
WINDBREAKER = NWToon(602910, 'mon')
COOKGO = NWToon(703849, 'mon')
JAMESONHILL = NWToon(671421, 'wed')
PINK = NWToon(715159, 'sat')
MAGICSCROLL = NWToon(655746, 'sun')
KILLERFOODS = NWToon(720117, 'sun')
SPERMAN = NWToon(730259, 'sun')



