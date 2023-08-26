### REST API
Technologies used 
- Django REST
- Heroku

### Setting Up the Environment

If possible, please have a look at this course: (Udemy Django REST course)[https://www.udemy.com/course/django-python-advanced/learn/lecture/32238716#overview]

- Install Docker Desktop
- Install VSCode

### Project Structure

#### ramuribackend

ramuribackend folder is the app in the project containing all the code shared between apps.

#### ramuriAPI

ramuriAPI folder is the app containing everything related to the brands and querying information.

### Virtual Environment

conda create --name ramuriapi

conda activate ramuriapi

conda install pip

pip install django

pip install djangorestframework

### If getting import errors

Make sure you are not in any other virtualenvironments before you activated conda, run:

`conda deactivate`

Alternatively, you might need to run:

`conda install -c conda-forge djangorestframework`

### Linting

run `flake8`

### Testing

run `python manage.py test`

## Creating requirements file for Heroku

`pip list --format=freeze > requirements.txt`


