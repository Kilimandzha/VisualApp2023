FROM python:3.10-slim
COPY requirements.txt ./requirements.txt
CMD cat requirements.txt
RUN pip install -r requirements.txt
COPY . ./
CMD gunicorn -b 0.0.0.0:8080 app.app:server