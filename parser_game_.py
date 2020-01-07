import requests                #эмуляция работы браузера
from pathlib import Path       #спец класс для работы с путями файловой системы

BASE_URL = 'http://forum.eve-ru.com/index.php?showtopic=111891'
BASE_SAVE_PATH = Path('./venv/eve_save')

r = requests.get(BASE_URL)     #передаем ссылку в эмулятор браузера, его мeтоду get
print(r.status_code)        #status of the answer/response

html_file_path = BASE_SAVE_PATH / 'eve_first.html'    #Путь до файла в переменную и имя файла после /

with open(str(html_file_path.absolute()), 'wb') as f:    # Открываем файл на запись с with (best practise)
    f.write(r.content)            #записываем в файл контент   # 'wb'  write binary запись в бинарном виде, f - Переменая файлика
'''этот код заходит на сайт по базовой ссылке, далее мы вручнуб создаем папку в этой же нашей папке проекта
и прописываем ее путь через BASE_SAVE_PATH = Path('./venv/eve_save'),далее библиотека requests заходит на базовыый url
отправляет запрос на сервер к статусу кода, потом в переменную мы записываем путь к файлу и имя самого файла, 
Который создается самой прогой. далее мы открывакм файл для биеарной записи туда инфы с сайта, конвертируем еше в строку путь
и пишем туда контент'''