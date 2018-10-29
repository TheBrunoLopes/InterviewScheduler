FROM alpine:3.7
WORKDIR /app
ADD . /app

RUN apk add --no-cache \
        python3 \
        python3-dev \
        gcc \
        make \
        libc-dev \
        musl-dev \
        linux-headers

#RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["uwsgi", "--http",":4001","-w", "application:application","-p","16"]
