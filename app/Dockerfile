FROM python:alpine3.22

WORKDIR /app

RUN apk add --no-cache \
    git \
    bash \
    curl

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["app.py"]
