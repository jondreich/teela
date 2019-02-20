# Teela

A [Flask](http://flask.pocoo.org/) bootstrap and application skeleton with [twelve-factor](http://www.12factor.net/) principles.

Bootstraps a typical Flask application with authentication, SQL database, forms and caching. Constructed of modular apps separating data modules, HTML-based views, JSON-based API responses and an authentication-protected admin interface.

Includes an `example` model for the purpose of demonstration SQL querying and basic CRUD admin actions. Basic templates and static file structure also in place.

### Dependencies

- [Flask](http://flask.pocoo.org/) - Python Web framework
- [Flask-SQLAlchemy](http://pythonhosted.org/Flask-SQLAlchemy) - Flask extension for [SQLAlchemy](http://www.sqlalchemy.org/)
- [Flask-Login](https://github.com/maxcountryman/flask-login) - user session management
- [Flask-WTF](https://flask-wtf.readthedocs.org/) - Flask integration with [WTForms](http://wtforms.readthedocs.org/)
- [Flask-Cache](http://pythonhosted.org/Flask-Cache/) - Cache extension for Flask
- [Flask-Script](http://flask-script.readthedocs.org/) - command-line tasks and scripts
- [Gunicorn](http://gunicorn.org/) - WSGI HTTP server
- [Honcho](https://github.com/nickstenning/honcho) - a Python clone of [Foreman](http://ddollar.github.com/foreman/)
- [Fabric](http://fabfile.org/) - command-line system admin, deployment, remote management
- [IPython](http://ipython.org/) - interactive shell

## Getting started

1. Install requirements (use [virtualenv](https://pypi.python.org/pypi/virtualenv))

        $ pip install -r requirements.txt

2. Initialise database with Fabric

        $ fab3 setup

3. Run with Fabric

        $ fab3 run

### Application and environment configuration

Honcho adds the contents of `.env` file as environment variables. The application boostrap configures Flask using these settings, so edit this file as you please - see [Flask configuration](http://flask.pocoo.org/docs/config/).

**Note:** Defaults are defined in [the config class](teela/config.py) for some settings, so you don't need to duplicate these in your `.env` if you want to keep it minimal. Currently `SERVER_NAME` (which is used to determine the application `HOST` and `PORT`), `SQLALCHEMY_DATABASE_URI` and `SECRET_KEY` are the only required settings.

Obviously, `SECRET_KEY` should be something considerably stronger than the example.

### Running locally

To run with Flask's development server, use:

    $ fab dev

Set `DEBUG=True` in your `.env` file to auto-reload with code changes. See the [fabfile](fabfile.py) for other commands.

#### See also:

- [Flask wiki](https://github.com/mitsuhiko/flask/wiki/Large-app-how-to), [Flask-skeleton](https://github.com/sean-/flask-skeleton) and [Fbone](https://github.com/imwilsonxu/fbone) for inspiration
- [The Twelve-Factor App](http://www.12factor.net/)
- [Declaring and Scaling Process Types with Procfile](https://devcenter.heroku.com/articles/procfile)
- [Dana](https://github.com/marchibbins/dana) - Django flavoured Twelve-Factor boilerplate

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0)