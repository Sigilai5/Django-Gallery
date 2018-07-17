# [Gallery]()
#### This is my Gallery
#### July 15th, 2018
#### By **[Brian Sigilai](https://github.com/sigilai5)**

## Description
This is a simple photo site where people can view diferent types of images.

## Set Up and Installations

### Prerequisites
1. Python3.6
2. Postgres
3. Python virtualenvironment
### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/Sigilai5/Django-Gallery.git`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE gallery;
```

```
### Run initial Migration
```bash
python3.6 manage.py makemigrations gram
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
No known bugs so far

## Technologies used
    - HTML
    - JavaScript
    - css
    - Python 3.6
    - Bootstrap 4
    - Heroku
    - Postgresql


### License
Copyright (c) **@Sigilai Brian**