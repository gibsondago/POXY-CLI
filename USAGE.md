# Cross-Platform Proxy Manager CLI - Complete Guide

This project provides a complete solution for managing HTTP/SOCKS proxies across Windows, macOS, and Linux with multiple usage options.

## Project Structure

```
proxy-cli/
├── .venv/                  # Python virtual environment
├── profiles/               # Directory for proxy profiles
├── config_manager.py       # Handles proxy profile configuration
├── proxy_server.py         # Implements local proxy server functionality
├── main.py                 # Main CLI application
├── requirements.txt        # Python dependencies
├── build.py                # Build script for creating executables
├── README.md               # Main documentation
├── proxy-cli.bat           # Windows convenience script
├── proxy-cli.sh            # Linux/macOS convenience script
├── install.bat             # Windows installation script
├── install.sh              # Linux/macOS installation script
└── dist/                   # Directory for built executables
    └── proxy-cli.exe       # Standalone executable (Windows)
```

## Installation

### Windows
Run the installation script:
```
install.bat
```

### Linux/macOS
Run the installation script:
```bash
chmod +x install.sh
./install.sh
```

Alternatively, you can manually set up the environment:
1. Create virtual environment: `python -m venv .venv`
2. Activate it: `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`

## Usage Options

### 1. Convenience Scripts (Recommended)
- **Windows**: `proxy-cli.bat <command> [options]`
- **Linux/macOS**: `./proxy-cli.sh <command> [options]`

### 2. Direct Python
- `python main.py <command> [options]` (or `python3` on some systems)

### 3. Standalone Executable
- `dist\proxy-cli.exe <command> [options]` (Windows)
- `dist/proxy-cli <command> [options]` (Linux/macOS - after building)

## Commands

- `add <name>` - Add a new proxy profile
- `list` - List all profiles
- `delete <name>` - Delete a profile
- `use <name> --mode <system|local>` - Activate a profile

## Examples

Add a proxy profile:
```
proxy-cli.bat add myproxy --type socks5 --host 127.0.0.1 --port 1080
```

List all profiles:
```
proxy-cli.bat list
```

Use a proxy locally:
```
proxy-cli.bat use myproxy --mode local
```

Use a proxy system-wide:
```
proxy-cli.bat use myproxy --mode system
```

## Building Executables

To create standalone executables without requiring Python:
```
python build.py
```

## Configuration Storage

Proxy profiles are stored in:
- Windows: `%USERPROFILE%\.proxy-cli\profiles.ini`
- macOS/Linux: `~/.proxy-cli/profiles.ini`

## Features

- Manage multiple proxy profiles
- Support for HTTP, SOCKS4, and SOCKS5 proxies
- System-wide and local proxy modes
- Cross-platform compatibility
- Virtual environment isolation
- Standalone executable distribution
- Convenience scripts for easy usage

## Troubleshooting

1. If getting "command not found" errors, ensure you're in the correct directory
2. If Python modules are missing, ensure the virtual environment is activated
3. For system proxy issues, ensure you have appropriate permissions (admin on Windows)
4. For local proxy issues, ensure the port is not in use

## License

MIT License - see LICENSE file for details.

## Author

**Rezaul Karim**  
Email: work.rezaul@outlook.com  
Powered By: REZ LAB