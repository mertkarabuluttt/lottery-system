#! /usr/bin/env bash
docker rm -f lottery-postgres-db
docker rm -f lottery-backend
docker volume rm -f lottery-system_db-data
docker network rm lottery-system_backend-postgres lottery-system_default
docker rmi -f lottery-system_web
