FROM python:3.10-slim
RUN apt-get update
RUN apt-get -y install gcc
WORKDIR /src
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r server_req.txt
CMD uvicorn server.application:app --host 0.0.0.0 --port 8000 --reload