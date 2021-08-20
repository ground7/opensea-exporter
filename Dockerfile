FROM python:3.9

WORKDIR /app
COPY requirements.txt .
COPY collector.py .

RUN pip install -r requirements.txt

EXPOSE 9000/tcp
ENV FLASK_APP=collector.py

CMD flask run -h 0.0.0.0 -p 9000