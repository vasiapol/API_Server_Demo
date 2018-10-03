FROM python:3-alpine
RUN apk add --update python3-dev gcc musl-dev linux-headers nginx
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3.7 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000/tcp
CMD ["uwsgi", "--ini", "API.ini"]

