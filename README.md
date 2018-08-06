# Python Flask

#### Table of contents

1. [Overview](#overview)
2. [Technologies](#technologies)
3. [Authors](#authors)
4. [Contributors](#contributors)
5. [Compatibility](#compatibility)
6. [Requirements](#requirements)
7. [Setup and Tasting](#setup-and-tasting)

## Overview

A simple application for tasting and findings on Docker Swarm cluster (docker-1.12+).

## Technologies

* Docker-1.12.0~rc4

## Authors

* Adriano Vieira (adriano.svieira at gmail.com)

## Contributors

* TBD

## Compatibility

Built on CEntOS-7 as base Docker image.

Moreover, we also have *debian8*, *python-2.7* and *Ubuntu-16* **Dockerfile** to build images, but these ones aren't supported.

### Tags

- **standard and supported**:
  - **centos7** (***latest***): built based on centos:7 image

#### PoC only
Proof of Concept for image sizes:
  - **debian8**: built based on debian:jessie image
  - **python27**: built based on python:2.7 image
  - **ubuntu16**: built based on ubuntu:xenial image

## Requirements

- Docker-1.12+ <https://docker.com>

## Setup and Tasting

First of all we need a host with Docker-1.12+ pre-installed and running. May be you could use one of my "Docker boxes" <https://app.vagrantup.com/adrianovieira> with built-in docker-1.12.

The docker images can be found on Docker Hub - <https://hub.docker.com/r/adrianovieira/flask/>

If you're familiar Docker with you could take it (e.g.: `docker pull adrianovieira/flask`) and play around.

If not, let me know how I can improve this ***doc***.

You'd take a look at my other project <https://github.com/adrianovieira/docker-swarm>.

### Proxy

If you are behind a proxy and is having problems pulling docker imagens... setup *Systemd Docker own Service*, as below (well done on CEntOS-7):

```bash
# setup docker service proxy (as root user)
mkdir -p /etc/systemd/system/docker.service.d
echo "[Service]" > /etc/systemd/system/docker.service.d/proxy.conf
echo "Environment='HTTPS_PROXY=$HTTP_PROXY' 'HTTP_PROXY=$HTTP_PROXY'" >> /etc/systemd/system/docker.service.d/proxy.conf
systemctl daemon-reload && systemctl restart docker
```

***keep CALMS and having fun***
