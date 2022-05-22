### Word search api using flask and docker.
### This api searches for the given word in a subtitle file.
### Returns a Json response contains the subtitle and its meta data.

### Installation
* Clone the repo
* create a venv => Python3 -m venv env
* activate the venv => source env/bin/activate
* Install the dependencies  => pip install -r requirements.txt
* start the app => docker-compose -f flask_compose.yml up
* Endpoint http://localhost:5000/search/<word to search>