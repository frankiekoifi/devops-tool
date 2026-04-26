# 🔧 FrankTechSpace DevOps Automation Tool

> **📖 For detailed installation instructions, see [INSTALLATION.md](INSTALLATION.md)**

A powerful, lightweight system monitoring and CI/CD pipeline automation tool.

## ✨ Features

- 📊 **Real-time system monitoring** (CPU, Memory, Disk, Network)
- 🔄 **CI/CD Pipeline automation** (Clone → Test → Build → Deploy)
- 🔔 **Smart alerting system** with thresholds
- 📈 **Historical data tracking**
- 🐳 **Docker ready**

## 📥 Installation

### One-Line Install (Linux/macOS)
curl -fsSL https://raw.githubusercontent.com/frankiekoifi/devops-tool/main/install.sh | bash

### One-Line Install (Windows PowerShell)
## powershell
irm https://raw.githubusercontent.com/frankiekoifi/devops-tool/main/install.ps1 | iex

## Manual Install
bash
# Clone the repository
git clone https://github.com/frankiekoifi/devops-tool.git

cd devops-tool

## Create Virtual Environment(Windows)
# Powershell

python -m venv venv

venv\Scripts\activate

# (Linux/macOS)

python3 -m venv venv

source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python backend/app.py

## 🚀 Usage

# Windowa

Start the tool:

# Terminal 1 - Backend Server
cd C:\Users\YOUR_USERNAME\franktechspace-devops\devops-tool

venv\Scripts\activate

python backend\app.py

Open your browser:

text

http://localhost:8001

# Terminal 2 - Frontend Dashboard (Open NEW terminal)
cd C:\Users\YOUR_USERNAME\franktechspace-devops\devops-tool\frontend

python -m http.server 5500

# Linux/macOS

# Terminal 1 - Backend Server
cd ~/franktechspace-devops/devops-tool

source venv/bin/activate

python backend/app.py

# Terminal 2 - Frontend Dashboard (Open NEW terminal)

cd ~/franktechspace-devops/devops-tool/frontend

python -m http.server 5500

# Open Browser

http://localhost:5500

View your system metrics in real-time!

## 📊 What You Can Monitor
- Metric	Description
- CPU Usage	Overall + per-core utilization
- Memory Usage	RAM and Swap usage
- Disk Usage	Storage space monitoring
- Network I/O	Data sent/received
- Top Processes	Most CPU-intensive tasks
- 🔄 CI/CD Pipeline
  
Trigger automated builds

Simulated test execution

Deployment tracking

Pipeline history

🔔 Alerts
Automatically triggered when:

CPU > 85% (Warning) / 95% (Critical)

Memory > 85% (Warning) / 95% (Critical)

Disk > 85% (Warning) / 95% (Critical)

## 🐳 Docker Deployment
bash

docker build -t devops-tool .

docker run -p 8001:8001 devops-tool

### 🛠️ Troubleshooting

## Port Already in Use

# Find process using port 8001 or 5500
netstat -ano | findstr :8001

# Kill the process (replace PID with actual number)
taskkill /PID 12345 /F

## 📁 Project Structure
text

devops-tool/
- ├── backend/
- │   ├── app.py          # Main FastAPI server
- │   ├── monitor.py      # System monitoring
- │   ├── pipeline.py     # CI/CD pipeline
- │   └── alerts.py       # Alert system
- ├── frontend/
- │   └── index.html      # Dashboard UI
- ├── install.sh          # Linux/macOS installer
- ├── install.bat         # Windows installer
- └── requirements.txt    # Python dependencies
  
## 🔗 Live Demo
Dashboard: https://devops-tool.netlify.app

API Docs: https://devops-tool-api.onrender.com/docs

### 📝 Uninstall

# Just delete the installation folder
rm -rf ~/franktechspace-devops   # Linux/macOS

rmdir /s C:\Users\YOUR_USERNAME\franktechspace-devops  # Windows

## 👨‍💻 Author
FrankTechSpace

Email: franktechspace@outlook.com

Phone: 0700 468 158

GitHub: @frankiekoifi

Built with 💚 by FrankTechSpace | Nairobi, Kenya

## 📄 License
MIT License - Free for personal and commercial use


