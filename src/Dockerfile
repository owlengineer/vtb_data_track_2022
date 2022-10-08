FROM python:3.8

COPY . app
WORKDIR app

RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install -r requirements.txt

CMD python3 api.py