FROM python:3.9

WORKDIR /app

RUN apt update \
    && apt install -y default-mysql-client

RUN python -m pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "app:app", "--reload"]