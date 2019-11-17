from utils import SIS
from models import *


if __name__ == '__main__':
    sis = SIS()
    #Toon = SLAMDUNK
    #Toon = NARUTO
    Toon = ONEPIECE
    Toon.generate_url()
    sis.set_title(Toon.title)
    sis.scrap_pages_with_parse(Toon, ".tmblr-full", "data-orig-src")
