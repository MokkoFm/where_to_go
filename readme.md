# Where to go - interesting places in Moscow

You can find and get more information about amazing places in Moscow.

## Installation

Python 3 must be installed. Download the code.

### Environment Variables 

Some of settings are taken from environment variables. Create `.env` near `manage.py` and write data there in this format:`VARIABLE=value`.

There're 3 variables:
- `SECRET-KEY` - project's secret key.
- `DEBUG` - (default:`False`) debug mode. Set `True` if you need to debug the project.
- `DATABASE` - project's name of database.

### Requirements

Install requirements with command:
```
pip install -r requirements.txt
```

## Running Code

Create SQLite database with command:
```
python manage.py migrate
```

Run development server with command:
```
python manage.py runserver
```

### Admin panel 

Create superuser with command:
```
python manage.py create superuser
```

Link to the admin panel: `http://127.0.0.1:8000/admin/`. 
You can add images and places there. 

## Project's Purposes

The code is written for educational purposes as a task in web-development course on the [Devman](https://dvmn.org/).
