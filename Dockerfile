FROM python:3.10.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/vin_machine

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/vin_machine

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "migrate" ]
