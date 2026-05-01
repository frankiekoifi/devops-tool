@echo off
echo Starting DevOps Tool Frontend...
echo.
echo Local Dashboard will open at http://localhost:5500
echo.
cd /d %~dp0
start http://localhost:5500/index-landing.html
python -m http.server 5500
pause