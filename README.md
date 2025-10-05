<div align="center">

# Proxy Manager CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/rezaulk/ProxyManagerCLI)

</div>

<div align="center">

A professional, cross-platform CLI tool for managing HTTP/SOCKS proxies across Windows, macOS, and Linux with beautiful, rich-formatted output.

</div>

<br/>

## ✨ Features

* **Manage multiple proxy profiles** - Create, list, and delete proxy configurations
* **Works across platforms** - Windows, macOS, and Linux support
* **Two activation modes** - System-wide and local proxy server modes
* **Supports multiple protocols** - HTTP, SOCKS4, SOCKS5 proxies
* **Beautiful UI** - Rich-formatted output with colors and tables
* **Authentication support** - Username/password authentication for proxies
* **Lightweight and portable** - Easy to install and distribute

## 📋 Prerequisites

- Python 3.6+ with pip
- Windows, macOS, or Linux operating system

## 🚀 Quick Start

### Installation

Choose one of the following methods:

#### Method 1: Using Installation Scripts (Recommended)
**On Windows:**
```bash
install.bat
```

**On Linux/macOS:**
```bash
chmod +x install.sh
./install.sh
```

#### Method 2: Manual Installation
1. Clone or download this repository
2. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

The proxy manager CLI can be used in three different ways:

### 1. Convenience Scripts (Recommended)
These scripts automatically handle virtual environment activation and provide enhanced formatting.

**On Windows:**
```bash
proxy-cli.bat <command> [options]
```

**On Linux/macOS:**
```bash
./proxy-cli.sh <command> [options]
```

### 2. Direct Python Execution
```bash
python main.py <command> [options]
```

### 3. Standalone Executable
```bash
# Windows
dist\proxy-cli.exe <command> [options]

# Linux/macOS
dist/proxy-cli <command> [options]
```

## 🧰 Commands

### Add a Proxy Profile
```bash
proxy-cli.bat add <name> --type <http|socks4|socks5> --host <proxy_host> --port <port_number> --username <username> --password <password>
```

**Examples:**
```bash
# Add an HTTP proxy
proxy-cli.bat add corporate_proxy --type http --host proxy.company.com --port 8080

# Add a SOCKS5 proxy with authentication
proxy-cli.bat add secure_proxy --type socks5 --host 192.168.1.100 --port 1080 --username myuser --password mypass
```

### List All Profiles
```bash
proxy-cli.bat list
```
Displays a formatted table with all proxy profiles and their details.

### Delete a Profile
```bash
proxy-cli.bat delete <name>
```

### Use a Proxy Profile
```bash
proxy-cli.bat use <name> --mode <system|local>
```

**System-wide proxy mode:**
Sets the proxy globally on your operating system.

**Local proxy server mode:**
Starts a local proxy server on `localhost:8080` that forwards to your configured proxy.

## 🎨 Visual Features

The CLI tool features beautiful, rich-formatted output including:
- Color-coded status messages
- Formatted tables for listing profiles
- Styled panels for important information
- Consistent formatting across all commands
- Interactive confirmation prompts (when available)

## 🏗️ Building Executables

To create a standalone executable:
```bash
python build.py
```

The executable will be created in the `dist/` folder and can be run without Python or dependencies.

## 📁 Project Structure

```
proxy-cli/
├── .venv/                  # Python virtual environment
├── profiles/               # Directory for proxy profiles
├── config_manager.py       # Handles proxy profile configuration
├── proxy_server.py         # Implements local proxy server functionality
├── main.py                 # Main CLI application with rich formatting
├── requirements.txt        # Python dependencies
├── build.py                # Build script for creating executables
├── README.md               # This documentation
├── USAGE.md                # Complete usage guide
├── proxy-cli.bat           # Windows convenience script
├── proxy-cli.sh            # Linux/macOS convenience script
├── install.bat             # Windows installation script
├── install.sh              # Linux/macOS installation script
└── dist/                   # Directory for built executables
    └── proxy-cli.exe       # Standalone executable (Windows)
```

## 🔧 Troubleshooting

1. **"Module not found" errors:** Ensure you activated the virtual environment
2. **Permission errors on Windows when setting system proxy:** Run as Administrator
3. **Rich formatting not working in some terminals:** The tool will still function but with basic text formatting
4. **For local proxy issues:** Verify that localhost:8080 is available and not in use by other applications

## 🧪 Tested On

- Windows 10/11 Command Prompt, PowerShell
- macOS Terminal
- Linux (Ubuntu, CentOS) Terminal

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Author

**Rezaul Karim**  
Email: work.rezaul@outlook.com  
Powered By: REZ LAB

## Project Structure

```
proxy-cli/
├── profiles/
├── config_manager.py     # Handles proxy profile configuration
├── proxy_server.py       # Implements local proxy server functionality
├── main.py               # Main CLI application
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Configuration File

Proxy profiles are stored in a configuration file:
- Windows: `%USERPROFILE%\.proxy-cli\profiles.ini`
- macOS/Linux: `~/.proxy-cli/profiles.ini`

## Dependencies

- `requests` - For HTTP requests (if needed in extensions)
- `pysocks` - For SOCKS proxy support
- `configparser` - For configuration file management
- `argcomplete` - For command-line argument completion (optional)

## Troubleshooting

1. **Permission errors on Windows when setting system proxy**:
   - Run the command prompt as Administrator
   - Or use local proxy mode instead

2. **Local proxy server not working**:
   - Make sure the specified local port (default 8080) is not in use
   - Check that your applications are configured to use localhost:8080 as the proxy

3. **SOCKS proxy issues**:
   - The current implementation has simplified SOCKS support
   - For full SOCKS functionality, consider using dedicated proxy tools

## Author

Author: Rezaul Karim
Email: work.rezaul@outlook.com
Powered By: REZ LAB
