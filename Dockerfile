FROM python:3.10-alpine
RUN apk add --no-cache tzdata
ENV TZ="Asia/Taipei"
WORKDIR /app
COPY get_crypto_price.py /app
RUN pip install pandas requests bs4
RUN mkdir -p /app/datasets
CMD ["python3","get_crypto_price.py"]
