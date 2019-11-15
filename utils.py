import requests
import os
from bs4 import BeautifulSoup as BS

N_PARSING_STR = '.wt_viewer img'


class PageLoader:
    def __init__(self, dir_name='default', url=None, extension='jpg'):
        self.url = url
        self.dir_name = dir_name
        self.parsing_str = N_PARSING_STR
        self.extension = extension
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        # 쿠키 추가하면 됨.
        self.cookies = 1
        
    def set_dir_name(self, dir_name):
        self.dir_name = dir_name

    def set_parsing_str(self, parsing_str):
        self.parsing_str = parsing_str

    def set_url(self, url):
        self.url = url

    def set_extension(self, extension):
        self.extension = extension

    def set_cookies(self, cookies):
        self.cookies = cookies
        self.headers.update({'cookie': self.cookies})

    def del_cookies(self):
        del self.headers['cookie']

    def scrap_page(self, url=None):
        os.makedirs(self.dir_name, exist_ok=True)
        if url:
            base_url = url
        else:
            base_url = self.url
        res = requests.get(base_url, headers=self.headers)
        soup = BS(res.text, 'html.parser')
        target_images = soup.select(self.parsing_str)

        for i in range(len(target_images)):
            with open(f'{self.dir_name}/{i}.{self.extension}', 'wb') as f:
                imgs = requests.get(target_images[i]['src'], stream=True, headers=self.headers)
                print(i, imgs.status_code)
                if imgs.status_code == 200:
                    f.write(imgs.raw.read())
                else:
                    continue

    def get_list(self, url, parsing_str):
        res = requests.get(url, headers=self.headers)
        soup = BS(res.text, 'html.parser')
        return soup.select(parsing_str)

    def dir_exist(self, dir_name):
        # dir이름이 존재하는지 boolean으로 알려주는 method
        pass


class SIS:
    def __init__(self, title='WebToon'):
        self.page_loader = PageLoader(dir_name=title)
        self.title = title

# Only implement Common Functions
    def scrap_pages(self, ToonModel, **kwargs):
        os.makedirs(self.title, exist_ok=True)
        os.chdir(self.title)

        if ToonModel.rate >= 18:
            if self.page_loader.cookies == 1:
                self.page_loader.set_cookies(kwargs['cookie'])

        for episode, url in ToonModel.url_generator():
            self.page_loader.set_dir_name(f'ep{episode}')
            self.page_loader.scrap_page(url)

        os.chdir('..')

    def set_title(self, title):
        self.title = title