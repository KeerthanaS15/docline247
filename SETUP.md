# Setting up the project

1. Set up the virtualenv.
1. Create new project "docline247"
1. Create new app "core"
1. Create custom user model
1. Install django-debug-toolbar
1. Install pylint and pylint-django
1. Install autopep8
1. Save pip-requirements

## Steps

```sh
# git clone
cd docline247

# create virtual environment
mkvirtualenv docline247

# install django LTS
pip install django==3.2.5

# create new project in current folder
django-admin startproject docline247 .

# create new app
django-admin core
```

Setup custom user model,

```python
# core/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

  class Meta:
    db_table = 'dl_users'
```

```python
# settings.py
AUTH_USER_MODEL = 'core.User'
```

Install django-debug-toolbar,

```sh
# install
pip install django-debug-toolbar

# configure: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
```

Install pylint and pylint-django

```sh
pip install pylint pylint-django

# setup vs code for pylint.
# refer to https://wiki.webinative.com/en/people/magesh-ravi/setting-up-a-django-project
```

Install autopep8

```sh
pip install autopep8
```
