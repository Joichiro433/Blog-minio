#!/bin/bash

docker-compose down

rm -rf minio_data
docker-compose up -d

mkdir -p minio_data/localbucket/image_dir/
cp -r image_dir/ minio_data/localbucket/image_dir/