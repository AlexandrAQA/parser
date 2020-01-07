import requests
from bs4 import BeautifulSoup as BS

def parser_games():

    ''' делаем parser он заходит на страницу лучших игр
     и считываеи все с 6 страниц и выводит в консоль
    '''

    max_page = 6     #кол-ва страниц для парсинга
    pages = []
    for x in range(1, max_page + 1): #проходим по всем страницам
        pages.append(requests.get('https://stopgame.ru/review/new/stopchoice/p' + str(x)))

    for r in pages:
        html = BS(r.content, 'html.parser')

        for el in html.select('.lent-block'):
            title = el.select('.lent-title > a')
            print(title[0].text)