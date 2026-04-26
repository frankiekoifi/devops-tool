@echo off
title DevOps Tool Launcher
color 0A

echo ============================================
echo    🔧 FRANKTECHSPACE DEVOPS TOOL 🔧
echo ============================================
echo.

echo [1/3] Starting Backend Server...
start "DevOps Backend" cmd /k "cd /d %~dp0 && venv\Scripts\activate && python backend\app.py"

echo [2/3] Waiting for backend to initialize...
timeout /t 3 /nobreak > nul

echo [3/3] Starting Frontend Dashboard...
start "DevOps Frontend" cmd /k "cd /d %~dp0\frontend && python -m http.server 5500"

echo.
echo Opening dashboard in your browser...
timeout /t 2 /nobreak > nul
start http://localhost:5500

echo.
echo ============================================
echo    ✅ BOTH SERVERS ARE RUNNING!
echo ============================================
echo    Backend API:  http://localhost:8001
echo    Frontend UI:  http://localhost:5500
echo ============================================
echo.
echo Close both terminal windows to stop.
echo.
pause