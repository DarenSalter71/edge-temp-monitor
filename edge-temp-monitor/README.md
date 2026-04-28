# Edge Temp Monitor v1

A Raspberry Pi CPU temperature monitoring and visualisation project built with Bash, Python Flask, and Chart.js.

This project collects temperature readings from a Raspberry Pi at scheduled intervals, stores the data locally, and presents it through a lightweight web dashboard with charts and trend history.

---

## 🚀 Overview

Edge Temp Monitor was created as a practical infrastructure / DevOps style project to demonstrate:

- Linux automation with Bash
- Cron scheduling
- Environment-based configuration
- Raspberry Pi hardware monitoring
- Python Flask web serving
- Frontend chart visualisation
- Structured logging and data collection
- Real-world monitoring workflow design

---

## ⚙️ Features

- Reads Raspberry Pi CPU temperature using:

bash vcgencmd measure_temp 

- Automated scheduled collection via cron
- Development / Production environment switching
- Historical logging of readings
- Flask web dashboard
- Interactive Chart.js graphing
- Threshold warning indicators
- Lightweight and low resource usage

---

## 🛠️ Tech Stack

- Bash
- Linux / Raspberry Pi OS
- Cron
- Python 3
- Flask
- HTML / CSS / JavaScript
- Chart.js

---

## 📁 Example Structure

text edge-temp-monitor/ ├── scripts/ │   └── pi-temp-monitor.sh ├── data/ │   └── readings.csv ├── templates/ │   └── index.html ├── app.py └── README.md 

---

## 🔄 How It Works

1. Cron runs the Bash script every X minutes  
2. Script captures current CPU temperature  
3. Reading is written to data file  
4. Flask reads the data source  
5. Dashboard displays trends in browser

---

## 📊 Example Use Cases

- Raspberry Pi health monitoring
- Edge device monitoring
- Learning Bash automation
- Learning Flask dashboards
- Temperature trend analysis
- Multi-device monitoring foundation

---

## 💡 What I Learned

- Bash scripting in production-style workflows
- Linux path / permission handling
- Cron troubleshooting and scheduling
- Separating dev vs prod configuration
- Integrating backend data with frontend charts
- Building complete end-to-end monitoring systems

---

## 🔭 Planned Future Versions

- SQL backend
- AWS cloud storage
- Multi-device support
- Telegram alerts
- Auto shutdown protection
- External ambient sensor support

---

## 👤 Author

Daren Salter

GitHub: DarenSalter71
