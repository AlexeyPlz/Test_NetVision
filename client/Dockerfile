FROM python:3.10-slim
RUN apt-get update
RUN apt-get -y install gcc
WORKDIR /src/client
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r client_req.txt
CMD python -m application