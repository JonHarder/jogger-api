# Jogger (API)
A REST backend server to store and query running information

## Instalation
The easiest way to get the server up and running is via a virtualenv
```
git clone https://github.com/JonHarder/jogger-api
python3 -m virtualenv jogger-venv
source jogger-venv/bin/activate
cd jogger-api
pip install -r requirements.txt
export FLASK_APP=jogger.py
flask run
```


## Features
* create and retrieve users (runners)
* create and retrieve sessions
 * all sessions
 * by session id


## TODO
* query jogging sessions by user
* query jogging sessions by date(range)?
