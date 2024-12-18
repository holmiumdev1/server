FROM python:3.13
WORKDIR /server
COPY app .
EXPOSE 6666
ENV PIP_ROOT_USER_ACTION=ignore
CMD pip3 install Flask; pip3 install gunicorn;gunicorn --bind 0.0.0.0:6666 app:app