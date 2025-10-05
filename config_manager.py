"""
Proxy Manager CLI - Configuration Manager

Author: Rezaul Karim
Email: work.rezaul@outlook.com
Powered By: REZ LAB

Handles proxy profile configuration.
"""

import os
import configparser
from pathlib import Path

CONFIG_DIR = Path.home() / ".proxy-cli"
CONFIG_FILE = CONFIG_DIR / "profiles.ini"

def init_config():
    CONFIG_DIR.mkdir(exist_ok=True)
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'w') as f:
            f.write("[DEFAULT]\n")

def add_profile(name, proxy_type, host, port, username=None, password=None):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    config[name] = {
        'type': proxy_type,
        'host': host,
        'port': str(port),  # Convert to string since configparser requires strings
        'username': username or '',
        'password': password or ''
    }
    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

def list_profiles():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.sections()

def get_profile(name):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if name in config:
        return dict(config[name])
    return None

def delete_profile(name):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if name in config:
        del config[name]
        with open(CONFIG_FILE, 'w') as f:
            config.write(f)