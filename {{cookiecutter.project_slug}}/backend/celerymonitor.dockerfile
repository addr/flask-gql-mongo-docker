FROM python:3.6

RUN pip install pipenv

COPY . /install
WORKDIR /install

ARG env=prod

RUN pipenv install --system --deploy

RUN bash -c 'if [ "$env" == "dev" ]; then pipenv install --system --deploy --dev; fi'

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

COPY ./app/monitor-start.sh /monitor-start.sh

RUN chmod +x /monitor-start.sh

CMD ["bash", "/monitor-start.sh"]
