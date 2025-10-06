<div align="center">

# 🚀 Poxy CLI - Advanced Proxy Management Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/rezaulwork/POXY-CLI)
[![GitHub Repo](https://img.shields.io/badge/repo-POXY--CLI-blue)](https://github.com/rezaulwork/POXY-CLI)

</div>

<div align="center">

**🔥 Professional Cross-Platform Proxy Manager CLI Tool** - Manage HTTP/SOCKS proxies with ease across Windows, macOS, and Linux. Features beautiful formatted output, multiple proxy protocols, authentication support, and both system-wide and local proxy server modes.

**[📥 Download](#-installation) • [📖 Usage Guide](#-usage) • [⭐ Features](#-features) • [🐛 Report Issues](https://github.com/rezaulwork/POXY-CLI/issues)**

</div>

<br/>

## 🔍 SEO Keywords

**proxy manager, proxy cli, proxy tool, socks proxy, http proxy, socks5 proxy, proxy configuration, cross-platform proxy, windows proxy, macos proxy, linux proxy, command line proxy, proxy server, proxy authentication, proxy profile management**

## ✨ Key Features & Benefits

🚀 **Multi-Platform Proxy Management**
* **Cross-platform compatibility** - Seamlessly works on Windows, macOS, and Linux
* **Multiple proxy protocols** - Full support for HTTP, SOCKS4, and SOCKS5 proxies
* **Dual operation modes** - System-wide proxy settings or local proxy server mode

🔧 **Advanced Proxy Configuration**
* **Profile management** - Create, list, modify, and delete proxy configurations easily
* **Secure authentication** - Username/password authentication for protected proxies
* **Flexible configuration** - Support for various proxy server types and settings

🎨 **Enhanced User Experience**
* **Rich formatted output** - Beautiful CLI interface with colors, tables, and styled panels
* **Intuitive commands** - Easy-to-use command-line interface for all operations
* **Interactive prompts** - User-friendly confirmation dialogs and guidance

📦 **Easy Installation & Deployment**
* **Lightweight and portable** - Minimal resource usage, easy to distribute
* **Multiple installation methods** - Scripts, manual installation, or standalone executables
* **No external dependencies** - Self-contained proxy management solution

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

The proxy manager CLI offers multiple ways to use it:

### 1. Interactive Menu Mode (Recommended for New Users)
Simply run the tool without any arguments to access the user-friendly menu:

**On Windows:**
```bash
proxy-cli.bat
```

**On Linux/macOS:**
```bash
./proxy-cli.sh
```

This opens an interactive menu with numbered options:
- **[1]** 📋 List all proxy profiles
- **[2]** ➕ Add a new proxy profile
- **[3]** 🗑️  Delete a proxy profile
- **[4]** ▶️  Use/Activate a proxy profile
- **[5]** ❓ Show help and usage information
- **[0]** ❌ Exit

### 2. Command Line Mode (For Advanced Users)
**On Windows:**
```bash
proxy-cli.bat <command> [options]
```

**On Linux/macOS:**
```bash
./proxy-cli.sh <command> [options]
```

### 3. Direct Python Execution
```bash
python main.py <command> [options]
```

### 4. Standalone Executable
```bash
# Windows
dist\proxy-cli.exe <command> [options]

# Linux/macOS
dist/proxy-cli <command> [options]
```

## 🧰 Commands

### Interactive Menu Mode (New!)
When you run the tool without arguments, you'll see an interactive menu:
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

### Command Line Mode

#### Add a Proxy Profile
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

#### List All Profiles
```bash
proxy-cli.bat list
```
Displays a formatted table with all proxy profiles and their details.

#### Delete a Profile
```bash
proxy-cli.bat delete <name>
```

#### Use a Proxy Profile
```bash
proxy-cli.bat use <name> --mode <system|local>
```

**System-wide proxy mode:**
Sets the proxy globally on your operating system.

**Local proxy server mode:**
Starts a local proxy server on `localhost:8080` that forwards to your configured proxy.

#### Show Help Information
```bash
# Access comprehensive help from the interactive menu (option 5)
# Or run the tool without arguments and select option 5
```

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

## 🔧 What's New

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

### 🛠️ Improved Launcher Scripts
- **Fixed pausing issues** - Scripts now only pause when showing the welcome menu
- **Better error handling** and user feedback
- **Cross-platform compatibility** improvements

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Author

**Rezaul Karim**  
Email: work.rezaul@outlook.com  
Powered By: REZ LAB

---
<div align="center">
  <strong>⭐ If you find this tool helpful, please consider giving it a star on GitHub!</strong>
</div>
