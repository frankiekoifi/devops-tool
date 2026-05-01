@echo off
echo ============================================
echo    🔧 FRANKTECHSPACE DEVOPS TOOL 🔧
echo ============================================
echo.

cd /d %~dp0

echo Activating virtual environment...
call venv\Scripts\activate

echo Starting backend server...
echo.

uvicorn backend.app:app --host 0.0.0.0 --port 8001 --reload

pause