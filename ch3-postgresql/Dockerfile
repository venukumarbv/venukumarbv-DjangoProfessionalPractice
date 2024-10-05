# Pull base image
FROM python:3.10.4-slim-bullseye

# Set environment variable
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set Working Directory
WORKDIR D:/Repos/DjangoForProfessionalPractice/ch3-postgresql

# Install Dependecies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .