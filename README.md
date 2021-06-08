# DevSecOps Challenge

This container accepts two unsorted or sorted arrays and joins them into single sorted array

```
ex: 
input:
[1,5,3] [9,4,7]
output:
[1, 3, 4, 5, 7, 9]
```

    Python programming langugage is used as backend program in the container to join arrays and python latest image from docker hub is used in dockerfile to build container

## Instructions to build container

1) Three files are inlcuded in the tarball 
```
joinArray.py
__main__.py
Dockerfile
```
2) Dockerfile describes the container required for this task
3) Run the below command to build the docker container
```
$docker build -t <name>:<tag> -f /path/to/dockerfile .
ex:
$docker build -t joinarray:1 -f /app .
```
4) After successful build, run the below command to run the container and join two arrays
```
$docker run <name>:<tag> array1 array2
ex:
$docker run joinarray:1 [1,2,3] [9,3,5]
output:
[1, 2, 3, 3, 5, 9]
```