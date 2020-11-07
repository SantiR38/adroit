# Adroit
=============

Online Store with employees management.


## Setting up on your local machine

For running this project it will be necesary to **download and install** the following things:

  1. [Python 3.6 32-bit](https://www.python.org/downloads/).
  2. [PostgreSQL](https://www.postgresql.org/download/).
  3. [Git](https://git-scm.com/download/win).
  4. [Pip](https://www.neoguias.com/como-instalar-pip-python/#Como_instalar_PIP_en_Windows).
  5. [Docker](https://docs.docker.com/engine/install/).
  6. [Docker-compose](https://docs.docker.com/compose/install/).


**Clone this project** in your local machine:

  7. Use `git clone` and the url of this project.


Make sure that **enviroment variables** are created. If not:

  8. Create the following files in `[root_directory]/.envs/.local/`: `.django` and `.postgres`.
  9. Declare the variables.

    .django:
      * REDIS_URL
      * CELERY_FLOWER_USER
      * CELERY_FLOWER_PASSWORD
    
    .postgres:
      * POSTGRES_HOST
      * POSTGRES_PORT
      * POSTGRES_DB
      * POSTGRES_USER
      * POSTGRES_PASSWORD


**Launch Docker**. You don't need to use docker commands because it's automated in `bash/` directory.

  10. Build the images with `$ source bash/build.sh`.
  11. Set up the processes with `$ source bash/up.sh`.


Next, you have to **create a superuser**:

  12. `$ source bash/django/createsuperuser.sh`.


## Work with django in an isolated terminal

  When you start your Docker container, the processes will be running in the same terminal.
  It's more confortable when you work with django in an isolated terminal so you can easily see
  the exceptions, and other messagges. Also you can kill and run Django whenever you want.
  
  Every time you start a container, open another terminal and run the follow commands.

  1. `$ export COMPOSE_FILE=local.yml`.
  2. `$ sudo docker-compose ps`. With this you are going to see a list of processes running in the container.
  3. Choose the name of Django process (example: adroit_django_2jk4123k) and run `$ sudo docker rm -f adroit_django_2jk4123k`.
  4. After that, run django `$ source bash/django/run.sh`
