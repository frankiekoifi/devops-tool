@echo off
title FrankTechSpace DevOps Tool Installer
color 0A

echo ===============================================================
echo    🔧 FRANKTECHSPACE - DEVOPS MONITORING TOOL 🔧
echo ===============================================================
echo.
echo    Real-time system metrics & monitoring dashboard
echo.
echo ===============================================================
echo.

REM Check Python installation
echo [INFO] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo [INFO] Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

python --version
echo [OK] Python found
echo.

REM Set installation directory
set INSTALL_DIR=%USERPROFILE%\franktechspace-devops
echo [INFO] Installation directory: %INSTALL_DIR%
mkdir "%INSTALL_DIR%" 2>nul
cd /d "%INSTALL_DIR%"

REM Clone or download repository
echo [INFO] Downloading DevOps Tool...
if exist "devops-tool" (
    echo [INFO] Updating existing installation...
    cd devops-tool
    git pull origin main
) else (
    git clone https://github.com/frankiekoifi/devops-tool.git
    cd devops-tool
)

REM Create virtual environment
echo [INFO] Creating Python virtual environment...
python -m venv venv

REM Activate and install dependencies
echo [INFO] Installing dependencies...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

REM Create start script
echo [INFO] Creating start script...
echo @echo off > start.bat
echo cd /d "%%~dp0" >> start.bat
echo call venv\Scripts\activate.bat >> start.bat
echo python backend/app.py >> start.bat
echo pause >> start.bat

echo.
echo ===============================================================
echo    🎉 INSTALLATION COMPLETE! 🎉
echo ===============================================================
echo.
echo    📌 To start monitoring:
echo       cd %INSTALL_DIR%\devops-tool
echo       start.bat
echo.
echo    📌 Then open browser to:
echo       http://localhost:8001
echo.
echo ===============================================================
echo    💡 Need help? Contact: franktechspace@outlook.com
echo ===============================================================
pause