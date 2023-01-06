FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1,PYTHONUNBUFFERED 1
COPY ./src /app
WORKDIR /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

