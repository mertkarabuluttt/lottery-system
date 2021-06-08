#! /usr/bin/env bash
docker-compose -f docker-compose-postgres.yml up -d
sleep 10
docker-compose -f docker-compose-backend.yaml up -d
