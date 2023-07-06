FROM python:3.10-slim
RUN apt-get update
RUN apt-get -y install gcc
WORKDIR /server
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn application:app --host 0.0.0.0 --port 8000 --reload