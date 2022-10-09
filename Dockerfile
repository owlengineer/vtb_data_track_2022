FROM python:3.8

COPY src src
WORKDIR src

RUN python3.8 -m pip install --upgrade pip
RUN pwd
RUN python3.8 -m pip install -r requirements.txt

CMD python3 api.py