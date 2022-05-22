# syntax=docker/dockerfile:1

#creating base image and workspace
FROM python:3

#creating a work directory
WORKDIR /my_api


#Installing dependencies
COPY requirements.txt /my_api/requirements.txt
RUN pip3 install -r /my_api/requirements.txt

#Copy app contents
COPY . /my_api


#start the app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


