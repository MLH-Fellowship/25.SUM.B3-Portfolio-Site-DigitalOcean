#!/bin/bash


PROJECT_DIR="$HOME/25.SUM.B3-Portfolio-Site-DigitalOcean/"
VENV_DIR="$PROJECT_DIR/venv"
SESSION_NAME="portfolio_site"

set -e

#pkill flask

tmux kill-server || echo "No active tmux server to kill."

echo "Changing to project directory: $PROJECT_DIR"
cd "$PROJECT_DIR"

echo "Fetching latest commit and resetting"
git fetch origin && git reset origin/main --hard


echo "Activating venv"
source "$VENV_DIR/bin/activate"

echo "Installing/updating Python dependencies from requirements.txt..."
pip install -r requirements.txt

deactivate

echo "Restarting myportfolio.service"
systemctl daemon-reload
systemctl restart myportfolio
systemctl status myportfolio
