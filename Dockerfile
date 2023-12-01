FROM python:3.6-alpine

WORKDIR /app

ENV PORT 9999

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
