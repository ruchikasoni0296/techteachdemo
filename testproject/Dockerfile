# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container


# Copy the requirements file into the container


# Install any dependencies
RUN pip install --upgrade pip
RUN apt-get update && pip install pkgconfig
FROM python:3.8
RUN apt-get update \
  && apt-get install -y default-libmysqlclient-dev default-mysql-client

WORKDIR /app



COPY requirements.txt /app/


 
RUN pip install -r requirements.txt

COPY . /app/

 
# RUN echo Hello
RUN rm -rf /var/lib/apt/lists/*

# Collect static files
RUN python manage.py collectstatic --noinput

# Copy the current directory contents into the container at /app
COPY . .



# Run the application
CMD python manage.py runserver