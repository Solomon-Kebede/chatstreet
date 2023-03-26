# Use Python base image
# FROM redis:5
FROM python:latest
# # Create app directory in Docker
WORKDIR /usr/src/app
COPY ./ChatStreetProject .
COPY ./requirements.txt .
EXPOSE 8000
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]