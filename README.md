* word search api using flask and docker.
* this api searches for the given word in a subtitle file.
* returns a Json response contains the subtitle and its meta data.

### local setup
* clone the repo
* create a venv => Python3 -m venv env
* activate the venv => source env/bin/activate
* install the dependencies  => pip install -r requirements.txt
* start the app => docker-compose -f flask_compose.yml up
* endpoint http://localhost:5000/search/<word to search>
