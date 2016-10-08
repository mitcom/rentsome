#!/usr/bin/env bash

docker rm -f rentsome-postgres
docker run \
    --name rentsome-postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e POSTGRES_USER=user \
    -e POSTGRES_DB=rentsome_db \
    -p 54321:5432 \
    -d postgres:9.5

# TODO:
# add conditional running migrations