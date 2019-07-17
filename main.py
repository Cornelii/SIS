import requests
from bs4 import BeautifulSoup as BS
from utils import PageLoader, SIS


if __name__ == '__main__':
    sis = SIS(title='수학 잘하는 법')
    sis.scrap_pages(1, 40)

