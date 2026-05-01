
````markdown
# 🔧 FrankTechSpace DevOps Automation Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-green.svg)](https://fastapi.tiangolo.com/)
[![Netlify](https://img.shields.io/badge/Netlify-Deployed-brightgreen.svg)](https://devops-tool.netlify.app)

A powerful, lightweight system monitoring and CI/CD pipeline automation tool for developers and system administrators.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 System Monitoring | Real-time CPU, Memory, Disk, Network |
| 🔄 CI/CD Pipeline | Clone → Test → Build → Deploy |
| 🔔 Smart Alerts | Threshold-based notifications |
| 📈 Historical Data | Track metrics (last 24h) |
| 🐳 Docker Ready | Containerized deployment |

---

## 📥 Installation

### Windows PowerShell

```powershell
irm https://raw.githubusercontent.com/frankiekoifi/devops-tool/main/install.ps1 | iex
````

### Linux/macOS

```bash
curl -fsSL https://raw.githubusercontent.com/frankiekoifi/devops-tool/main/install.sh | bash
```

### Manual Install

```bash
git clone https://github.com/frankiekoifi/devops-tool.git
cd devops-tool

pip install -r requirements.txt
python -m backend.app
```

---

## 🚀 Usage

```bash
python -m backend.app
```

Open in browser:

```
http://localhost:8001
```

---

## 🌍 Live Demo

* Dashboard: [https://devops-tool.netlify.app](https://devops-tool.netlify.app)
* API: [https://devops-tool-api.onrender.com](https://devops-tool-api.onrender.com)
* Docs: [https://devops-tool-api.onrender.com/docs](https://devops-tool-api.onrender.com/docs)

⚠️ Demo uses cloud server metrics (not your local machine)

---

## 📊 Monitoring

| Metric  | Description    | Threshold    |
| ------- | -------------- | ------------ |
| CPU     | Per-core usage | 85% / 95%    |
| Memory  | RAM + Swap     | 85% / 95%    |
| Disk    | Storage        | 85% / 95%    |
| Network | I/O            | Monitor only |

---

## 🔄 CI/CD Pipeline

1. Clone repository
2. Install dependencies
3. Run tests
4. Build application
5. Deploy

(All stages simulated)

---

## 🔔 Alerts

* Real-time dashboard alerts
* Severity levels (Warning / Critical)
* Acknowledge + history tracking

---

## 🐳 Docker

```bash
docker build -t devops-tool .
docker run -p 8001:8001 devops-tool
```

---

## 📁 Project Structure

```text
devops-tool/
├── backend/
│   ├── app.py
│   ├── monitor.py
│   ├── pipeline.py
│   └── alerts.py
├── frontend/
├── install.sh
├── install.ps1
├── install.bat
├── requirements.txt
└── README.md
```

---

## 🛠️ Requirements

* Python 3.8+
* pip
* Browser
* Docker (optional)

---

## 🐛 Troubleshooting

| Issue                 | Fix                         |
| --------------------- | --------------------------- |
| ImportError           | Use `python -m backend.app` |
| Port in use           | Kill process on 8001        |
| Dashboard not loading | Ensure backend is running   |

---

## 👨‍💻 Author

FrankTechSpace

* Email: franktechspace@outlook.com
* GitHub: @frankiekoifi
* Location: Nairobi, Kenya

---

## 📄 License

MIT License © 2026 FrankTechSpace

---

## ⭐ Support

* Star the repo
* Share with developers
* Open issues or suggestions

Built with Francis Ochieng💚 in Nairobi, Kenya
