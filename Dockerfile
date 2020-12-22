FROM python:3.8-alpine

RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv > /dev/null && \
    pipenv install --dev --system
COPY . .
