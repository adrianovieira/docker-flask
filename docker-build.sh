#!/bin/bash

echo "INFO: [docker-compose.sh] build simple flask image"
if [[ "$HTTP_PROXY" != "" && "$HTTP_PROXY" != "http://proxy_not_set:3128" ]]; then
  ENVIRONMENT="--build-arg https_proxy=$HTTP_PROXY --build-arg http_proxy=$HTTP_PROXY"
fi

docker build $ENVIRONMENT -t adrianovieira/flask$2 $1 .
