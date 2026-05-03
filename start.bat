@echo off
title FrankTechSpace DevOps Tool
cd /d "%~dp0"

call venv\Scripts\activate.bat

python -m backend.app

pause
