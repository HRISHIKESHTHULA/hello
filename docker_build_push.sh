#!/usr/bin/env bash

git clone https://github.com/HRISHIKESHTHULA/hello.git
sudo yum install git
sudo yum install docker
sudo systemctl restart docker
cd hello/
sudo docker build -t hrishikeshthula/hello_world:latest .
sudo docker login
sudo docker push hrishikeshthula/hello_world:latest
