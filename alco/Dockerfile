# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY alco/ alco/




# Copy the current directory contents into the container at /code/
COPY . /code/


EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
