FROM python:3.10.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y \
  wget \
  vim

RUN pip install --upgrade pip
COPY ./app/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./compose/start.sh /start
RUN chmod +x /start

WORKDIR /app
