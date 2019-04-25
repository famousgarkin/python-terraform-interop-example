FROM alpine
RUN apk update && apk add python3 terraform ca-certificates
CMD true
