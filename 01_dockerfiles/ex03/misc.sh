#!/bin/bash

docker build -t "gitlab-perso" .
docker create -ti -p 22001:22 -p 80:80 -p 443:443 --privileged --name gitlab gitlab-perso
docker start gitlab
docker logs --follow gitlab
docker exec -ti gitlab /bin/bash
