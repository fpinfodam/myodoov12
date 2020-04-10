#!/bin/bash

local_web=./docker/volumes/myodoov11_odoo-web-data/_data
remote_web=/var/lib/odoo

local_db=./docker/volumes/myodoov11_odoo-db-data/_data
remote_db=/var/lib/postgresql/data

container_web=myodoov11_web_1
container_db=myodoov11_db_1

docker cp $local_web $container_web:$remote_web

docker cp $local_db $container_db:$remote_db
