# dockerfile for prod
# dockerfile for testing the bulding (docker build -t image-name .)
# NB: It doesn't include connections to the DB

# Define image to build from
FROM python:3.6-slim

# Docker set up maintainer 
LABEL AUTHOR="scott/seggie <dev@resource.org>"
LABEL app="resource-idea-api"

ENV PYTHONUNBUFFERED 1

# Create directory to hold the application code inside the image
RUN mkdir /code

# change to directory
WORKDIR /code

# set 8000 as port and expose it
ENV PORT=8000
EXPOSE 8000

# Copy requirements files
COPY requirements.txt requirements.dev.txt /code/

# Install requirements
RUN pip install -r requirements.txt requirements.dev.txt

# Copy all project files to the working directory
COPY . /code/

# launch the application
CMD ["python" "manage.py" "runserver" "0.0.0.0:8000"]