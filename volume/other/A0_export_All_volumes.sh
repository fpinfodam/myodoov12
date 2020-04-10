#!/bin/bash

docker run --rm -it -v /Users/OscarIglo/volume-backup:/backup -v /var/lib/docker:/docker alpine:edge tar cfz /backup/volumes.tgz /docker/volumes/

