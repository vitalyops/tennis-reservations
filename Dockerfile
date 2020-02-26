FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /usr/src/app
COPY . .
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "server.py"]
