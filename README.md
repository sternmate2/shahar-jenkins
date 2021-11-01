# Alison

Alison is a dns-to-tls proxy server in python.
Currently Alison listens on port 8888 and supports only cloudflare.

# Features
TCP and UCP listeres
Client concurrency
Validate DNS input

### Implementation

Event loop based concurrency:
    * Class ClientContext - Takes care of the client
    * Class Upstream - Takes care of connecting and querying nameserver (cloudflare in this case)
    There are more classes, but they are the important ones.

### Possible features/Addons
* Connection pool to backend
* Handeling Signals
* Metrics
* Tests
* Caching
* Better logging and handeling exceptions
* Reconnect on failure

### Security concerns

* DNS spoofing
* Malicious input
* App running as privileged user (in Dockerfile app is running as user 'alison')

### Integration in microservice architecture

This proxy should run as a sidecar to some dns caching service (DNSMasq for example).

## Installing
Alison is distributed as a python command line tool. just copy this repo using 'git clone', and run the following command in the root directory of the project:
```
pip3 install .
```

## CMD
Alison will listen on port 8888 for udp and tcp
```
alison --tcp --udp

               _ _  
         /\   | (_) VERSION 0.0.1
        /  \  | |_ ___  ___  _ __ 
       / /\ \ | | / __|/ _ \| '_ \ 
      / ____ \| | \__ \ (_) | | | |  
     /_/    \_\_|_|___/\___/|_| |_|  
                   jonatanzafar59@gmail.com  

2018-10-24 08:40:55,328 INFO  Alison started on 127.0.0.1:8888

```

## DOCKER
build the docker image using the following command:
```
docker build -t alison .
```
then you can run Alison as a docker container using:
```
docker run -p 8888:8888/TCP -p  8888:8888/UDP alison
```

## BUILD
the build process is coded into .travis.yml, it includes:
* installing requirements.txt
* running tests
* building the docker image
* pushing to aws ECR


# DEPLOY
* the CI will redeploy the FARGATE container after push to ECR (cluster: sample-cluster, service: alison-udp)