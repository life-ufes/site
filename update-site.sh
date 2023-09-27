#!/bin/bash
git pull
docker restart blog
docker-compose up -d
