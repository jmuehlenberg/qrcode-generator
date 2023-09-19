#!/bin/bash

# Check for root privileges
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root."
   exit 1
fi

# Update Package Repository
echo "Updating package repositories..."
sudo apt update || { echo "Updating failed, exiting." ; exit 1; }

# Install qrcode-generator Dependencies
echo "Installing qrencode and imagemagick..."
sudo apt-get install qrencode imagemagick -y || { echo "Installing qrencode and imagemagick failed, exiting." ; exit 1; }

# Install Python dependencies
echo "Installing Python dependencies..."
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y || { echo "Installing Python dependencies failed, exiting." ; exit 1; }

# Install Python 3
echo "Installing Python 3..."
sudo apt install python3 -y || { echo "Installing Python 3 failed, exiting." ; exit 1; }

# Install Python 3 PIP
echo "Installing PIP for Python 3..."
sudo apt install python3-pip -y || { echo "Installing PIP for Python 3 failed, exiting." ; exit 1; }

# Install Tkinter for Python 3
echo "Installing Tkinter for Python 3..."
sudo apt-get install python3-tk -y || { echo "Installing Tkinter for Python 3 failed, exiting." ; exit 1; }

echo "All packages installed successfully."
