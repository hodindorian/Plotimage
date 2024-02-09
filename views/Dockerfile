FROM ubuntu:20.04

ENV TZ=Europe/Paris

ENV PYTHONUNBUFFERED=1

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt upgrade

RUN apt install -y python3 python3-pip python3-tk && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install django numpy pillow

COPY . /app

EXPOSE 8000

WORKDIR /app

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
