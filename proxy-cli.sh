#!/bin/bash

# Proxy Manager CLI Shell Script for Linux/macOS

echo
echo "##########################"
echo "# Proxy Manager CLI Tool #"
echo "##########################"
echo

# Change to the script's directory
cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "[INFO] Creating virtual environment..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to create virtual environment."
        echo "Please make sure Python 3 is installed."
        exit 1
    fi
    
    echo "[INFO] Installing dependencies..."
    source .venv/bin/activate
    pip install -r requirements.txt >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install dependencies."
        exit 1
    fi
    echo "[INFO] Setup complete!"
    echo
fi

# Activate the virtual environment
source .venv/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to activate virtual environment."
    exit 1
fi

# Run the main Python script with all arguments
python3 main.py "$@"

# Check if this was a 'use' command with local mode
if [[ "$*" == *"use"*"--mode"*"local"* ]]; then
    echo
    echo "NOTE: Local proxy server is running. Press Ctrl+C to stop."
    echo
else
    # For other commands, pause to show output
    echo
    echo "Press Enter to continue..."
    read
fi

# Deactivate the virtual environment
deactivate