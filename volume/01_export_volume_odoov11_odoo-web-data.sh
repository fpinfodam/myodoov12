#!/bin/bash

local_dir=$(pwd)
docker_dir=/var/lib/docker

web=myodoov11_odoo-web-data
db=myodoov11_odoo-db-data

docker run --rm -it -v $local_dir:/backup -v $docker_dir:/docker alpine:edge tar cfz /backup/$web.tgz /docker/volumes/$web/
docker run --rm -it -v $local_dir:/backup -v $docker_dir:/docker alpine:edge tar cfz /backup/$db.tgz /docker/volumes/$db/
