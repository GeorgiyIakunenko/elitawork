FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "elita_work.wsgi:application", "--bind", "0.0.0.0:8010"]
