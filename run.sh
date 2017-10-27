#!/bin/bash
docker build -t test -f python3.Dockerfile .
docker run -ti -v $(pwd):/opt test
