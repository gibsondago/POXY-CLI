#!/bin/bash

# Installation script for Proxy Manager CLI on Linux/macOS

echo
echo "####################################################"
echo "# Proxy Manager CLI - Installation Script (Linux/macOS)"
echo "####################################################"
echo

# Change to the script's directory
cd "$(dirname "$0")"

echo "[1] Creating virtual environment..."
python3 -m venv .venv
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to create virtual environment."
    echo "Make sure Python3 is installed."
    exit 1
fi

echo "[2] Installing dependencies..."
source .venv/bin/activate
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies."
    exit 1
fi

echo "[3] Making scripts executable..."
chmod +x proxy-cli.sh install.sh
if [ $? -ne 0 ]; then
    echo "[WARNING] Failed to make script executable."
fi

echo "[4] Testing the installation..."
./proxy-cli.sh --help
if [ $? -ne 0 ]; then
    echo "[WARNING] There might be an issue with the installation."
fi

echo
echo "[SUCCESS] Installation completed successfully!"
echo
echo "You can now use the proxy manager CLI with:"
echo "  - ./proxy-cli.sh (Linux/macOS shell script)"
echo "  - Directly with: python3 main.py"
echo "  - Standalone executable: dist/proxy-cli (after building)"
echo
echo "To add your first proxy profile:"
echo "  ./proxy-cli.sh add myproxy --type http --host proxy.example.com --port 8080"
echo