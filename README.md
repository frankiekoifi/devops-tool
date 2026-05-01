# 🔧 FrankTechSpace DevOps Automation Tool

A powerful, lightweight system monitoring and CI/CD pipeline automation tool.

---

## ✨ Features

- 📊 Real-time system monitoring (CPU, Memory, Disk, Network)
- 🔄 CI/CD Pipeline automation (Clone → Test → Build → Deploy)
- 🔔 Smart alerting system with thresholds
- 📈 Historical data tracking
- 🐳 Docker ready

---

## 📥 Installation

### One-Line Install (Linux/macOS)

```bash
curl -fsSL https://raw.githubusercontent.com/frankiekoifi/devops-tool/main/install.sh | bash
One-Line Install (Windows PowerShell)
irm https://raw.githubusercontent.com/frankiekoifi/devops-tool/main/install.ps1 | iex
Manual Install
git clone https://github.com/frankiekoifi/devops-tool.git

cd devops-tool

pip install -r requirements.txt

python backend/app.py
🚀 Usage
python backend/app.py

Open in browser:

http://localhost:8001
📊 What You Can Monitor
Metric	Description
CPU Usage	Overall + per-core utilization
Memory Usage	RAM and Swap usage
Disk Usage	Storage space monitoring
Network I/O	Data sent/received
Top Processes	Most CPU-intensive tasks
🔄 CI/CD Pipeline
Trigger automated builds
Simulated test execution
Deployment tracking
Pipeline history
🔔 Alerts

Triggered when:

CPU > 85% (Warning) / 95% (Critical)
Memory > 85% (Warning) / 95% (Critical)
Disk > 85% (Warning) / 95% (Critical)
🐳 Docker Deployment
docker build -t devops-tool .

docker run -p 8001:8001 devops-tool
📁 Project Structure
devops-tool/
├── backend/
│   ├── app.py
│   ├── monitor.py
│   ├── pipeline.py
│   └── alerts.py
├── frontend/
│   └── index.html
├── install.sh
├── install.bat
└── requirements.txt
🔗 Live Demo
Dashboard: https://devops-tool.netlify.app
API Docs: https://devops-tool-api.onrender.com/docs
👨‍💻 Author

FrankTechSpace

Email: franktechspace@outlook.com
Phone: 0700 468 158
GitHub: @frankiekoifi
📄 License

MIT License – Free for personal and commercial use