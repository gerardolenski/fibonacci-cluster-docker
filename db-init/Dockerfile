FROM python:3.12.6-bullseye
WORKDIR /app

RUN set -eux; \
    apt-get update; \
    pip install psycopg2-binary;
COPY ./db-init.py ./db-init.py
ENTRYPOINT ["sh", "-c", "python3 db-init.py"]