#!/bin/bash
# scripts/run_local.sh

echo "🔥 Starting Restaurant AI POC with Docker Compose..."
docker-compose down
docker-compose build
docker-compose up
