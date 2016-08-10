# Python Flask

## Overview

Please, also take a look on our [README](https://github.com/adrianovieira/docker-flask/blob/master/README.md).

## Docker Flask (python) fidings

This is the first version (v0.1.0)

- if you have `docker swarm` running:  
  `docker service create -p 80:80 --replicas 3 --name appHelloFlask adrianovieira/flask`

***or***

- *"standalone"*:  
  `docker run -d -p 80:80 --name appHelloFlask adrianovieira/flask`

 You could use some Flask environment variable to customize something  
 (e.g `docker run --env FLASK_DEBUG=1 -d -p 80:80 --name appHelloFlask adrianovieira/flask`).

Source code: <https://github.com/adrianovieira/docker-flask>

## Tags

- **standard and supported**:
  - **centos7** (***latest***): built based on centos:7 image (*[Dockerfile](https://github.com/adrianovieira/docker-flask/blob/master/Dockerfile)*)

----

### PoC only
Proof of Concept for image sizes:
  - **debian8**: built based on *debian:jessie* image (*[Dockerfile-debian8](https://github.com/adrianovieira/docker-flask/blob/master/Dockerfile-debian8)*)
  - **python27**: built based on *python:2.7* image (*[Dockerfile-python17](https://github.com/adrianovieira/docker-flask/blob/master/Dockerfile-python27)*)
  - **ubuntu16**: built based on *ubuntu:xenial* image (*[Dockerfile-ubuntu16](https://github.com/adrianovieira/docker-flask/blob/master/Dockerfile-ubuntu16)*)

***keep CALMS and having fun***
