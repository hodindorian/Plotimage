FROM python:3.8

ENV TZ=Europe/Paris

ENV PYTHONUNBUFFERED=1

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get autoclean && apt-get update && apt-get clean && apt-get autoremove

RUN apt install -y python3-tk && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install django numpy pillow

COPY . /app

EXPOSE 8000

WORKDIR /app

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
