@echo off
REM Installation script for Proxy Manager CLI on Windows

echo ##################################################
echo # Proxy Manager CLI - Installation Script (Windows)
echo ##################################################
echo.

REM Change to the script's directory
cd /d "%~dp0"

echo [1] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found.
    echo Please install Python from https://www.python.org/ and make sure it's in your PATH.
    pause
    exit /b 1
)

echo [2] Creating virtual environment...
python -m venv .venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment.
    echo Make sure Python is installed and in your PATH.
    pause
    exit /b 1
)

echo [3] Installing dependencies...
call .venv\Scripts\activate.bat
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b 1
)

echo [4] Making scripts executable...
REM On Windows, batch files are executable by default
echo [INFO] Scripts are ready to use.

echo [5] Testing the installation...
proxy-cli.bat --help
if errorlevel 1 (
    echo [WARNING] There might be an issue with the installation.
)

echo.
echo [SUCCESS] Installation completed successfully!
echo.
echo You can now use the proxy manager CLI with:
echo   - proxy-cli.bat (Windows batch script)
echo   - Directly with: python main.py
echo   - Standalone executable: dist\proxy-cli.exe
echo.
echo To add your first proxy profile:
echo   proxy-cli.bat add myproxy --type http --host proxy.example.com --port 8080
echo.
echo For interactive mode, simply run:
echo   proxy-cli.bat
echo.
pause