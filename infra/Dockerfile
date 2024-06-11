FROM python:3.12.4-alpine

ENV POETRY_VERSION=1.7.1

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apk add --no-cache \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile=minimal && \
    source $HOME/.cargo/env && \
    pip install --upgrade pip && \
    pip install --no-cache-dir poetry==${POETRY_VERSION} && \
    poetry install --no-root && \
    apk del \
        curl \
        libressl-dev \
        musl-dev

RUN rm -rf /app/tests

EXPOSE 8080

CMD ["poetry", "run", "fastapi", "run", "main.py", "--port", "8080"]
