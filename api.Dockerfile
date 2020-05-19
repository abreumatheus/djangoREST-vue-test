FROM tiangolo/meinheld-gunicorn:python3.8
WORKDIR /django_api/
COPY ./django_api /app

RUN pip install -r /app/requirements.txt
