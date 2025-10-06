# 🚀 Cross-Platform Proxy Manager CLI - Complete Usage Guide

A comprehensive guide for managing HTTP/SOCKS proxies across Windows, macOS, and Linux with an intuitive interactive menu system and powerful command-line interface.

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Installation Methods](#-installation-methods)
- [Interactive Menu Guide](#-interactive-menu-guide)
- [Command Line Reference](#-command-line-reference)
- [Advanced Usage](#-advanced-usage)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)

## 🚀 Quick Start

### For New Users (Interactive Menu)
Simply run the tool without any arguments:

**Windows:**
```bash
proxy-cli.bat
```

**Linux/macOS:**
```bash
./proxy-cli.sh
```

This opens a user-friendly menu with numbered options (0-5) for easy proxy management.

### For Advanced Users (Command Line)
```bash
# Windows
proxy-cli.bat <command> [options]

# Linux/macOS
./proxy-cli.sh <command> [options]
```

## 📦 Installation Methods

### Method 1: Automated Installation (Recommended)
**Windows:**
```bash
install.bat
```

**Linux/macOS:**
```bash
chmod +x install.sh
./install.sh
```

### Method 2: Manual Installation
1. Create virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate virtual environment:
   ```bash
   # Linux/macOS
   source .venv/bin/activate

   # Windows
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Interactive Menu Guide

When you run the tool without arguments, you'll see:

```
🚀 Welcome to Proxy Manager CLI

Available Options:
[1] 📋 List all proxy profiles
[2] ➕ Add a new proxy profile
[3] 🗑️  Delete a proxy profile
[4] ▶️  Use/Activate a proxy profile
[5] ❓ Show help and usage information
[0] ❌ Exit
```

### Menu Option Details:

#### [1] List All Proxy Profiles
- Displays a formatted table with all saved proxy configurations
- Shows profile name, type, host, port, and authentication status
- Color-coded for easy reading

#### [2] Add a New Proxy Profile
**Interactive prompts for:**
- Profile name (must be unique)
- Proxy type (HTTP, SOCKS4, SOCKS5)
- Proxy host/IP address
- Proxy port number (1-65535)
- Username (optional)
- Password (optional, if username provided)

**Features:**
- Input validation for all fields
- Helpful error messages
- Confirmation of successful creation

#### [3] Delete a Proxy Profile
**Interactive process:**
- Lists all available profiles for selection
- Shows profile details (type, host, port)
- Requires confirmation before deletion
- Provides feedback on success/failure

#### [4] Use/Activate a Proxy Profile
**Two activation modes:**

**Local Mode (Recommended):**
- Starts a local proxy server on `localhost:8080`
- Forwards traffic to your configured proxy
- No admin privileges required
- Configure applications to use `localhost:8080`

**System Mode:**
- Sets system-wide proxy settings
- Affects all applications
- Requires administrator/root privileges
- May need application restarts

#### [5] Help and Usage Information
- Comprehensive help documentation
- Feature explanations and tips
- Security best practices
- Command-line examples
- Troubleshooting guidance

## 💻 Command Line Reference

### Basic Commands

#### Add a Proxy Profile
```bash
proxy-cli.bat add <name> --type <http|socks4|socks5> --host <host> --port <port> [options]
```

**Required Parameters:**
- `name`: Unique name for the proxy profile
- `--type`: Proxy type (`http`, `socks4`, `socks5`)
- `--host`: Proxy server host/IP
- `--port`: Proxy server port (1-65535)

**Optional Parameters:**
- `--username`: Authentication username
- `--password`: Authentication password

**Examples:**
```bash
# HTTP proxy without authentication
proxy-cli.bat add work-http --type http --host proxy.company.com --port 8080

# SOCKS5 proxy with authentication
proxy-cli.bat add secure-socks5 --type socks5 --host 192.168.1.100 --port 1080 --username myuser --password mypass
```

#### List All Profiles
```bash
proxy-cli.bat list
```
Displays a formatted table with all proxy profiles.

#### Delete a Profile
```bash
proxy-cli.bat delete <name>
```
**Example:**
```bash
proxy-cli.bat delete old-proxy
```

#### Use/Activate a Profile
```bash
proxy-cli.bat use <name> --mode <system|local>
```

**Examples:**
```bash
# Start local proxy server
proxy-cli.bat use work-proxy --mode local

# Set system-wide proxy (requires admin)
proxy-cli.bat use work-proxy --mode system
```

## 🔧 Advanced Usage

### Multiple Usage Methods

#### 1. Convenience Scripts (Recommended)
- **Windows**: `proxy-cli.bat <command> [options]`
- **Linux/macOS**: `./proxy-cli.sh <command> [options]`

#### 2. Direct Python Execution
```bash
python main.py <command> [options]
# or
python3 main.py <command> [options]
```

#### 3. Standalone Executable
```bash
# Windows
dist\proxy-cli.exe <command> [options]

# Linux/macOS (after building)
dist/proxy-cli <command> [options]
```

### Building Standalone Executables

Create executables that don't require Python:

```bash
python build.py
```

The executable will be created in the `dist/` folder.

## ⚙️ Configuration

### Configuration File Locations
- **Windows**: `%USERPROFILE%\.proxy-cli\profiles.ini`
- **macOS/Linux**: `~/.proxy-cli/profiles.ini`

### Configuration Format
```ini
[profile_name]
type = socks5
host = 192.168.1.100
port = 1080
username = myuser
password = mypass
```

## 🛠️ Project Structure

```
proxy-cli/
├── .venv/                  # Python virtual environment
├── profiles/               # Directory for proxy profiles
├── config_manager.py       # Handles proxy profile configuration
├── proxy_server.py         # Implements local proxy server functionality
├── main.py                 # Main CLI application with rich formatting
├── requirements.txt        # Python dependencies
├── build.py                # Build script for creating executables
├── README.md               # Main documentation
├── USAGE.md                # This detailed usage guide
├── proxy-cli.bat           # Windows convenience script
├── proxy-cli.sh            # Linux/macOS convenience script
├── install.bat             # Windows installation script
├── install.sh              # Linux/macOS installation script
└── dist/                   # Directory for built executables
    └── proxy-cli.exe       # Standalone executable (Windows)
```

## 🔍 Features Overview

### ✨ Interactive Menu System
- **User-friendly numbered options** (0-5) for easy navigation
- **Guided workflows** for all proxy management tasks
- **Input validation** and helpful error messages
- **Rich visual formatting** with colors and emojis

### 📚 Comprehensive Help System
- **Detailed usage documentation** accessible from the menu (option 5)
- **Complete feature overview** with explanations
- **Security best practices** and troubleshooting tips
- **Command-line examples** for advanced users

### 🛠️ Enhanced Proxy Management
- **Multiple proxy protocols**: HTTP, SOCKS4, SOCKS5
- **Dual operation modes**: System-wide and local proxy server
- **Secure authentication**: Username/password support
- **Profile management**: Create, list, modify, delete configurations
- **Cross-platform compatibility**: Windows, macOS, Linux

### 🎨 Visual Features
- **Rich formatted output** with colors and styled panels
- **Formatted tables** for profile listings
- **Interactive confirmation prompts**
- **Consistent formatting** across all commands

## 🚨 Troubleshooting

### Common Issues

#### 1. "Module not found" errors
**Solution:** Ensure virtual environment is activated
```bash
# Check if activated
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

#### 2. Permission errors on Windows (System Proxy)
**Solution:** Run as Administrator
```bash
# Right-click Command Prompt → "Run as administrator"
# Or use local mode instead
```

#### 3. Local proxy server not working
**Solutions:**
- Ensure port 8080 is available and not in use
- Check that applications are configured for `localhost:8080`
- Verify firewall settings allow local connections

#### 4. Rich formatting not displaying correctly
**Solution:** The tool functions normally, just without colors in some terminals

#### 5. Launcher script issues (Fixed in latest version)
**Note:** Recent updates fixed pausing issues in launcher scripts

### Getting Help

1. **Interactive Menu**: Run the tool and select option 5
2. **Command Line**: Access help through the menu system
3. **Documentation**: Check README.md for quick reference
4. **Examples**: See command examples throughout this guide

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Author

**Rezaul Karim**  
Email: work.rezaul@outlook.com  
Powered By: REZ LAB

---

<div align="center">
  <strong>⭐ Found this guide helpful? Consider starring the project on GitHub!</strong>
</div>
