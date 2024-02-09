FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN wget http://fr.archive.ubuntu.com/ubuntu/pool/universe/p/python-stdlib-extensions/python-tk_2.7.18-1_amd64.deb

RUN pip install --upgrade pip

RUN pip install django numpy pillow

COPY . /app

EXPOSE 8000

WORKDIR /app

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
