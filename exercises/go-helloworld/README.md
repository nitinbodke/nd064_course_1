# Go Hello World

This is a simple Go web application that prints a "Hello World" message.

## Run the application

This application listens on port `6111`

To run the application, use the following command:
```
go run main.go 
```

Access the application on: http://127.0.0.1:6111/

## Solution:
Commands to build and upload docker image:
```
cd exercises/go-helloworld
# Add following command to Dockerfile, which is missing in instructions
# RUN go mod init

# Build image
docker build -t go-helloworld .

# Run image locally
# Last part of the command is command to run and its arguments, hence following do not work!
# docker run -d -p 6111:6111  go-helloworld --name helloworld
docker run -d -p 6111:6111 --name helloworld go-helloworld

# Test
curl http://localhost:6111/

# Find container details
docker ps | grep helloworld

# Stop docker
docker stop helloworld

# Tag
# docker tag <repo>:<tag>  <repo>:<tag>>
docker tag go-helloworld  nitinbodke/lab:v0.1.0

# Push
docker push nitinbodke/lab:v0.1.0

# pull image nitinbodke/lab:v0.1.0
docker pull nitinbodke/lab:v0.1.0

# run
docker run -d -p 6111:6111 --name hello nitinbodke/lab:v0.1.0

# stop 
docker stop hello

# delete image
docker rmi nitinbodke/lab/go-helloworld:v0.1.0
```