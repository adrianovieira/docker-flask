#!/bin/bash -x

if [[ -f /etc/os-release  ]]; then
  . /etc/os-release
fi

if [[ "$ID" == "centos" && "$VERSION_ID" == "7" ]]; then

  if [[ "$HTTP_PROXY" != "" && "$HTTP_PROXY" != "http://proxy_not_set:3128" ]]; then
    echo "INFO: [docker-setup-proxy.sh] setting docker service proxy ($HTTP_PROXY)"
    sudo mkdir -p /etc/systemd/system/docker.service.d
    sudo echo "[Service]" > /tmp/proxy.conf
    sudo echo "Environment='HTTPS_PROXY=$HTTP_PROXY' 'HTTP_PROXY=$HTTP_PROXY' 'no_proxy=\"127.0.0.1, localhost\"'" >> /tmp/proxy.conf
    sudo mv /tmp/proxy.conf /etc/systemd/system/docker.service.d/proxy.conf
    sudo systemctl daemon-reload && sudo systemctl restart docker
  fi

fi

if [[ "$?" == 0 ]]; then
  echo "INFO: [docker-setup-proxy.sh] finished successfuly"
else
  exit 1
fi
