# locuss-backend

[![Build Status](https://travis-ci.org/ClemSau/locuss-backend.svg?branch=master)](https://travis-ci.org/ClemSau/locuss-backend)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)
[![Maintainability](https://api.codeclimate.com/v1/badges/cb28e0803652681915a1/maintainability)](https://codeclimate.com/github/ClemSau/locuss-backend/maintainability)

Backend of the Locuss flashcard app. Check out the project's [documentation](http://ClemSau.github.io/locuss-backend/).

Checkout the project's [roadmap](https://www.notion.so/00c82ffee92749479b71709e74ac8a14?v=b153bab6ceb248ad8c7ef0c7199315c9)

The [locuss-frontend](https://github.com/ClemSau/locuss-frontend) repository is also open to contributions

## Table of content

- [Project structure](#project-structure)
- [Get started](#get-started)
    - [Prerequisites](#prerequisites)
    - [Local development](#local-development)
- [Deployment](#deployment)   

## Project structure

```
/api
    /cards      # Card model application
    /common     # Mixins
    /config     # Django configuration
    /decks      # Deck model application
    /users      # User model application
/docs
/requirements
.coveragerc
.dockerignore
.gitignore
.travis.yml
docer-compose.yml
Docerfile
manage.py
mkdocs.yml
README.md
setup.cfg
wait_for_postgres.py
```

## Get started

### Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

### Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a bash shell in the container:
```
docker-compose run --rm web bash
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

## Deployment

The application is deployed on [heroku](https://www.heroku.com/)