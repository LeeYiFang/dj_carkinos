# Carkinos

Django refactor for Carkinos project.


## Getting Started

### Requirements

- Git
- Python 3.4+

### Set up a Python Virtual Environment

#### Built-in `venv`

Create the virtual environment at `<repo>/venv`:

    python3 -m venv venv

To activate it:

    . venv/bin/activate

Or on Windows, use

    . venv\Scripts\activate.bat

#### Anaconda or Miniconda

NOTE: Requires more setting.

They are the same but anaconda comes with more packages at the downloading time
and bigger size. [Anaconda] manages both the pacakges and Python version itself
via [conda].

To create a conda-based virtual environment, use

    conda create -n venv python=3.5

And activate it

    . activate venv

Or on Windows, use command-line console and run

    activate venv


### Install Dependencies

Use pip:

    pip install -r requirements.txt


### Set up Local Environment Variables and Database

Settings are stored in environment variables via [django-environ]. The
quickiest way to start is to copy `local.sample.env` into `local.env`:

    cp src/pycontw2016/settings/local.sample.env src/pycontw2016/settings/local.env

Then edit the `SECRET_KEY` line in `local.env`, replacing `{{ secret_key }}` into any [Django Secret Key] value. An example:

    SECRET_KEY=-@5#xz3#f)4waw+p=l^c$1!6ei8&c5u_=^%*sdu(6vy@m$*-v&

After that, just run the migration.


### Go Develop

Change to the `src` directory:

    cd src

Run database mirgration:

    python manage.py migrate

Run the development server

    python manage.py runserver


[Anaconda]: https://www.continuum.io/downloads
[conda]: http://conda.pydata.org/docs/intro.html
[django-environ]: http://django-environ.readthedocs.org/en/latest/
[Django Secret Key]: http://www.miniwebtool.com/django-secret-key-generator/
