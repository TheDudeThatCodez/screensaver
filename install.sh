#!/bin/bash

set -e

USERNAME=$(whoami)
SERVICE_NAME=rotating-screensaver

echo "Installing dependencies..."

sudo apt update
sudo apt install -y cmatrix hollywood sl bb libcaca0 aview cbonsai nyancat

echo "Copying files..."

sudo cp rotating_screensaver.py /usr/local/bin/rotating_screensaver.py
sudo chmod +x /usr/local/bin/rotating_screensaver.py

cp rotating-screensaver.service /tmp/${SERVICE_NAME}.service
sed -i "s|REPLACE_ME|$USERNAME|g" /tmp/${SERVICE_NAME}.service
sudo mv /tmp/${SERVICE_NAME}.service /etc/systemd/system/${SERVICE_NAME}.service

echo "Enabling systemd service..."

sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable ${SERVICE_NAME}
sudo systemctl start ${SERVICE_NAME}

echo "✅ Done! Rotating CLI screensaver is running on tty1."
