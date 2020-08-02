FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential curl
WORKDIR /usr/src/app
COPY . .
EXPOSE 5000
RUN pip3 install -r requirements.txt
CMD ["python", "server.py"]
