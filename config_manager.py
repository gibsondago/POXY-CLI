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
from typing import Dict, List, Optional

CONFIG_DIR = Path.home() / ".proxy-cli"
CONFIG_FILE = CONFIG_DIR / "profiles.ini"

def init_config() -> None:
    """Initialize the configuration directory and file."""
    CONFIG_DIR.mkdir(exist_ok=True)
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'w') as f:
            f.write("[DEFAULT]\n")

def add_profile(name: str, proxy_type: str, host: str, port: int, username: Optional[str] = None, password: Optional[str] = None) -> None:
    """Add a new proxy profile to the configuration.

    Args:
        name: Unique name for the proxy profile
        proxy_type: Type of proxy (http, socks4, socks5)
        host: Proxy server hostname or IP address
        port: Proxy server port number
        username: Optional authentication username
        password: Optional authentication password
    """
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

def list_profiles() -> List[str]:
    """List all available proxy profile names.

    Returns:
        List of profile names (section names from config)
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.sections()

def get_profile(name: str) -> Optional[Dict[str, str]]:
    """Get a proxy profile by name.

    Args:
        name: Name of the proxy profile to retrieve

    Returns:
        Dictionary containing profile data, or None if not found
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if name in config:
        return dict(config[name])
    return None

def delete_profile(name: str) -> None:
    """Delete a proxy profile.

    Args:
        name: Name of the proxy profile to delete
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if name in config:
        del config[name]
        with open(CONFIG_FILE, 'w') as f:
            config.write(f)
