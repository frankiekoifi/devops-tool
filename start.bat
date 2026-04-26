@echo off
title FrankTechSpace DevOps Tool
color 0A

echo ==============================================
echo    🔧 FRANKTECHSPACE DEVOPS TOOL 🔧
echo ==============================================
echo.
echo Starting DevOps Monitoring System...
echo.

:: Get the current directory
set "ROOT_DIR=%~dp0"
set "ROOT_DIR=%ROOT_DIR:~0,-1%"

:: Start Backend Server
echo [1/3] Starting Backend API Server...
start "DevOps Backend" cmd /k "cd /d "%ROOT_DIR%" && venv\Scripts\activate && python backend\app.py"

:: Wait for backend to initialize (5 seconds)
echo [2/3] Waiting for backend to start...
timeout /t 5 /nobreak > nul

:: Start Frontend Server
echo [3/3] Starting Frontend Dashboard...
start "DevOps Frontend" cmd /k "cd /d "%ROOT_DIR%\frontend" && python -m http.server 5500"

:: Wait a moment then open browser
timeout /t 2 /nobreak > nul

:: Open browser to dashboard
echo Opening dashboard in your browser...
start http://localhost:5500

echo.
echo ==============================================
echo    ✅ ALL SYSTEMS RUNNING!
echo ==============================================
echo.
echo Backend API:  http://localhost:8001
echo Frontend UI:  http://localhost:5500
echo.
echo Close both terminal windows to stop.
echo ==============================================
echo.
pause