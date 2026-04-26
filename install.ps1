# FrankTechSpace DevOps Tool Installer for Windows PowerShell

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "    🔧 FRANKTECHSPACE - DEVOPS MONITORING TOOL 🔧" -ForegroundColor Yellow
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""
Write-Host "    Real-time system metrics & monitoring dashboard" -ForegroundColor White
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "📌 Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ $pythonVersion found" -ForegroundColor Green
}
catch {
    Write-Host "❌ Python not found. Please install Python 3.8 or higher" -ForegroundColor Red
    exit 1
}

# Set installation directory
$installDir = "$env:USERPROFILE\franktechspace-devops"
Write-Host "📁 Creating installation directory: $installDir" -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path $installDir | Out-Null
Set-Location $installDir

# Clone repository
Write-Host "📥 Downloading DevOps Tool..." -ForegroundColor Yellow
if (Test-Path "devops-tool") {
    Write-Host "Updating existing installation..." -ForegroundColor Yellow
    Set-Location devops-tool
    git pull origin main
}
else {
    git clone https://github.com/frankiekoifi/devops-tool.git
    Set-Location devops-tool
}

# Create virtual environment
Write-Host "🐍 Creating Python virtual environment..." -ForegroundColor Yellow
python -m venv venv

# Install dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
& "$installDir\devops-tool\venv\Scripts\Activate.ps1"
pip install --upgrade pip
pip install -r requirements.txt

# Create start script
Write-Host "🚀 Creating start script..." -ForegroundColor Yellow
$startScript = @'
@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
python backend/app.py
pause
'@
$startScript | Out-File -FilePath "start.bat" -Encoding ascii

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Green
Write-Host "🎉 INSTALLATION COMPLETE! 🎉" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Green
Write-Host ""
Write-Host "📌 To start monitoring YOUR computer:" -ForegroundColor Yellow
Write-Host "   cd $installDir\devops-tool" -ForegroundColor White
Write-Host "   start.bat" -ForegroundColor White
Write-Host ""
Write-Host "📌 Then open your browser to:" -ForegroundColor Yellow
Write-Host "   http://localhost:8001" -ForegroundColor White
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "💡 Need help? Contact: franktechspace@outlook.com" -ForegroundColor Yellow
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan