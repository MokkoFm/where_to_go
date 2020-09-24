# Where to go - interesting places in Moscow

You can find and get more information about amazing places in Moscow.
[Web-site](https://mokkofm.pythonanywhere.com/) of the project.

## Installation

Python 3 must be installed. Download the code.

### Environment Variables 

Some of settings are taken from environment variables. Create `.env` near `manage.py` and write 2 variables there in this format:`VARIABLE=value`.

- `SECRET_KEY=your secret key`
- `DEBUG=True or False` - (default:`False`) debug mode. Set `True` if you need to debug the project.

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

## Admin panel 

Create superuser with command:
```
python manage.py create superuser
```

Link to the admin panel: `http://127.0.0.1:8000/admin/`. 
You can add images and places there. 

## How to upload new place by command 

You can use special command:
```
python manage.py load_place "url_to_json"
```
Information in JSON should be like this:
```
{
    "title": "Title of the place",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        ...
    ],
    "description_short": "Short description of the place",
    "description_long": "Long description of the place",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

## Project's Purposes

The code is written for educational purposes as a task in web-development course on the [Devman](https://dvmn.org/).
