#!/usr/bin/env python3
"""
Build script for Proxy Manager CLI
Creates a standalone executable using PyInstaller

Author: Rezaul Karim
Email: work.rezaul@outlook.com
Powered By: REZ LAB
"""

import os
import subprocess
import sys
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller is already installed.")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully.")

def build_executable():
    """Build the executable using PyInstaller"""
    install_pyinstaller()
    
    # Path to the main script
    main_script = "main.py"
    
    if not Path(main_script).exists():
        print(f"Error: {main_script} not found!")
        return False
    
    print("Building executable...")
    
    # Create the build command
    build_cmd = [
        "pyinstaller",
        "--onefile",           # Create a single executable file
        "--name", "proxy-cli", # Name of the executable
        "--distpath", "dist",  # Output directory
        main_script
    ]
    
    try:
        # Use python -m PyInstaller instead of direct pyinstaller command
        subprocess.check_call([sys.executable, "-m", "PyInstaller"] + build_cmd[1:])
        print("Executable built successfully!")
        print(f"Find your executable in the 'dist' folder: {Path('dist') / 'proxy-cli.exe'}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during build: {e}")
        return False

def main():
    """Main function to run the build process"""
    print("Proxy Manager CLI - Build Script")
    print("=" * 40)
    
    success = build_executable()
    
    if success:
        print("\nThe proxy manager CLI is now available as a standalone executable.")
        print("You can also use the convenience scripts:")
        print("  - proxy-cli.bat (Windows)")
        print("  - proxy-cli.sh (Linux/macOS)")
        print("\nFor usage instructions, run: proxy-cli.exe --help")
    else:
        print("\nBuild failed. Please check the error messages above.")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())