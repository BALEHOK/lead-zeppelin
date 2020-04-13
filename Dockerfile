# Image to install and compile dependencies
FROM python:3.7-alpine as compile

RUN apk update && \
    apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev

RUN pip install --upgrade pip

WORKDIR /usr/src/app

# The app image
FROM compile

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]

