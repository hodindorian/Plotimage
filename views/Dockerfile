FROM ubuntu:16.04

ENV PYTHONUNBUFFERED=1

RUN apt install -y python3-tk && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install django numpy pillow

COPY . /app

EXPOSE 8000

WORKDIR /app

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
