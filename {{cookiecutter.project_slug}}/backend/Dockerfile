FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install pipenv

COPY . /install
WORKDIR /install

RUN pipenv install --system --deploy

COPY ./app /app
WORKDIR /app/

EXPOSE 80
