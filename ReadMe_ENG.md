# Data Prediction Server

This project consists of a Flask-based server that provides forecasts about the departure of customers from the RZD. It includes a Reactos web interface and a Python backend that uses a pre-trained model for forecasting.

## Project Structure

├── site/ # Frontend code \
└── server/ # Backend code \
ㅤㅤㅤ├── dist/ # Compiled code \
ㅤㅤㅤ├── functions.py \
ㅤㅤㅤ├── model.py \
ㅤㅤㅤ└── runserver.py \


## Technology Stack

- ReactJS
- SASS, Bootstrap
- Python 3.8
- Flask, Pandas, Numpy
- LightGBM, XGBoost, CatBoost.


## Installation

1. Clone this repository:
```sh
    git clone <repository-url>
    cd <project-directory>
```

2. Install frontend dependencies:
```sh
    cd site
    npm install
```


3. Install backend dependencies:
```sh
    cd ../server
    pip install -r requirements.txt
```

## Building the Project

1. Build the frontend:

```sh
    cd site
    npm run build
    npm run postbuild
```


2. Build the backend:

```sh
    cd ../server
    pyinstaller --name runserver --onefile runserver.py
```


## Running the Application

After building, you can run the application by executing the compiled `runserver` file in the `server/dist` directory.

On Windows:

```
server\dist\runserver.exe
```

On macOS/Linux:

```
./server/dist/runserver
```

The server will start and automatically open a web browser to `http://127.0.0.1:5000/index.html`.

## API Endpoints

- `GET /data/<location>`: Returns the top 20 companies for which the forecast of leaving RZD is the highest