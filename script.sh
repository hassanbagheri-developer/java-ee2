#!/bin/bash

echo test
[root@centos8 java-ee1]# cat script.sh2
#!/bin/bash

docker images | grep firstweb_image
echo ---------------------------
echo
docker ps -a | grep firstweb_image
echo
for i in `docker ps -a | grep firstweb_image | awk '{print $1}'`
do
        docker rm -f $i
done

for i in `docker images | grep firstweb_image | awk '{print $3}'`
do
        docker rmi -f $i
done
