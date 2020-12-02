FROM python:3 AS builder
LABEL maintainer="ANDRE F.C. MELO"

RUN pip install cmake
RUN pip install dlib

ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

FROM python:3
COPY --from=builder /opt/webapp .

RUN pip install gunicorn
RUN pip install Flask
RUN pip install Jinja2
RUN pip install Werkzeug
RUN pip install numpy
RUN pip install face-recognition

CMD gunicorn --bind 0.0.0.0:5000 wsgi
