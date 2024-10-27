# Сервер прогнозирования данных

Этот проект состоит из сервера на базе Flask, который предоставляет прогнозы об уходе клиентов из компании РЖД. Он включает веб-интерфейс на ReactJS и серверную часть на Python, которая использует предварительно обученную модель для прогнозирования.

## Структура проекта

├── site/ # Внешний код \
└── server/ # серверный код \
ㅤㅤㅤ├── dist/ # Скомпилированный код \
ㅤㅤㅤ├── functions.py \
ㅤㅤㅤ├── model.py \
ㅤㅤㅤ└── runserver.py \


## Технологический стек

- ReactJS
- SASS, Bootstrap
- Python 3.8
- Flask, Pandas, Numpy
- LightGBM, XGBoost, CatBoost.


## Установка

1. Клонируем этот репозиторий:
```sh
    git clone <repository-url>
    cd <project-directory>
```

2. Установите интерфейсные зависимости:
```sh
    cd site
    npm install
```


3. Установите серверные зависимости:

```sh
    cd ../server
    pip install -r requirements.txt
```

## Создание проекта

1. Создайте интерфейс:

```sh
    cd site
    npm run build
    npm run postbuild
```


2. Создайте серверную часть:

```sh
    cd ../server
    pyinstaller --name runserver --onefile runserver.py
```


## Запуск приложения

После сборки вы можете запустить приложение, выполнив скомпилированный файл "runserver" в каталоге "server/dist".

В Windows:

```
server\dist\runserver.exe
```

В macOS/Linux:

```
./server/dist/runserver
```

Сервер запустится и автоматически откроет веб-браузер для `http://127.0.0.1:5000/index.html`.

## API

- `GET /data/<location>`: Возвращает топ 20 компаний для которых прогноз ухода из РЖД наивысший