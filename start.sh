#!/bin/bash

docker image build -t mbi_api .
docker run --name mbi -p 5000:5000 --net=host -d mbi_api
