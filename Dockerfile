FROM python:3-alpine
WORKDIR /usr/src/app
RUN apk add --update python3-dev gcc musl-dev linux-headers
COPY . .
RUN pip3.7 install --no-cache-dir -r requirements.txt
EXPOSE 5000/tcp
CMD ["uwsgi", "--ini", "API.ini"]
