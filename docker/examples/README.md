

## Basic Python App

### Basic

Need to uncomment main_0().

Build tagged image and run it.

```bash
$ cd ./basic_python_app
$ docker build --tag app:0.1 --force-rm . --file ./Dockerfile
$ docker run --rm app:0.1
```

### Basic + Args

Need to uncomment main_1().

Build tagged image and run it with args.

```bash
$ cd ./basic_python_app
$ docker build --tag app:0.1 --force-rm . --file ./Dockerfile
$ docker run --rm app:0.1 --n 10
```

## Flask Python App

Build tagged image and run it with port forwarding.

```bash
$ cd ./basic_flask_app
$ docker build --tag app:0.1 --force-rm . --file ./Dockerfile
$ docker run -p 8001:5000 --rm --name app_cont app:0.1
```

Run and detach container (run as daemon) and management.

```bash
$ docker run -d -p 8001:5000 --rm --name app_cont app:0.1 
``` 

To stop and remove container.

```bash
$ docker stop app_cont
$ docker rm app_cont
```

## Remove dangling images

```bash
$ docker rmi $(docker images -qa -f 'dangling=true')
```










