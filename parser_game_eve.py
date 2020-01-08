import requests                #эмуляция работы браузера
from pathlib import Path       #спец класс для работы с путями файловой системы

BASE_URL = 'http://forum.eve-ru.com/index.php?showtopic=111891&page={page_num}' #add &page={page_num}
BASE_SAVE_PATH = Path('./venv/eve_save')

for i in range(1,4):      #add cicle for 3 pages
    r = requests.get(BASE_URL.format(page_num=i))   #add .format(page_num=i)
    print(r.status_code)

    html_file_path = BASE_SAVE_PATH / 'eve_first_{page_num}.html'.format(page_num=i)    #add _{page_num}.html'.format(page_num=i) creating 3 file instead 1

    with open(str(html_file_path.absolute()), 'wb') as f:    # Открываем файл на запись с with (best practise)
        f.write(r.content)            #записываем в файл контент   # 'wb'  write binary запись в бинарном виде, f - Переменая файлика
