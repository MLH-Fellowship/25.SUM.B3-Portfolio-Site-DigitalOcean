#!/bin/bash


PROJECT_DIR="$HOME/25.SUM.B3-Portfolio-Site-DigitalOcean/"
VENV_DIR="$PROJECT_DIR/venv"
SESSION_NAME="portfolio_site"

set -e

#pkill flask

echo "Changing to project directory: $PROJECT_DIR"
cd "$PROJECT_DIR"

echo "Fetching latest commit and resetting"
git fetch origin && git reset origin/main --hard


echo "Spinning down any currently active docker containers"
docker compose -f docker-compose.prod.yml down
echo "Starting up production docker container"
docker compose -f docker-compose.prod.yml up -d --build
