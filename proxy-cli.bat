@echo off
REM Proxy Manager CLI Windows Batch Script

echo.
echo ##########################
echo # Proxy Manager CLI Tool #
echo ##########################
echo.

REM Change to the script's directory
cd /d "%~dp0"

REM Check if virtual environment exists
if not exist ".venv" (
    echo [INFO] Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment.
        echo Please make sure Python is installed and in your PATH.
        pause
        exit /b 1
    )
    
    echo [INFO] Installing dependencies...
    call .venv\Scripts\activate.bat
    pip install -r requirements.txt >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] Failed to install dependencies.
        pause
        exit /b 1
    )
    echo [INFO] Setup complete!
    echo.
)

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Check if activation was successful
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to activate virtual environment.
    echo Please make sure you have created the virtual environment with 'python -m venv .venv'
    echo.
    pause
    exit /b 1
)

REM Run the main Python script with all arguments
python main.py %*

REM Check if this was a 'use' command with local mode
echo %* | findstr /i "use.*--mode.*local" >nul
if not errorlevel 1 (
    echo.
    echo NOTE: Local proxy server is running. Press Ctrl+C to stop.
    echo.
    goto :end
)

REM For other commands, pause to show output
echo.
echo Press any key to continue...
pause >nul

:end