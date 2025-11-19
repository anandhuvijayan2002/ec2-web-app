# AWS EC2 Python Web App

A simple Python Flask web application deployed on an AWS EC2 (Free Tier) Ubuntu instance.  
This project demonstrates how to host a web application, configure systemd services, and expose the app to the internet using EC2 Security Groups.

---

## 🚀 Features
- Python Flask web app
- Hosted on AWS EC2 (Ubuntu 22.04)
- Accessible via Public IP on port 5000
- Configured using systemd (`webapp.service`)
- Beginner-friendly deployment steps

---

## 📁 Project Structure
ec2-web-app/
├── app.py
├── requirements.txt
└── README.md

---

## 🎯 Endpoints
### `/`
Displays:Hello from AWS EC2!
This app is running on Ubuntu (Free Tier)


### `/about`
Shows:anandhu vijayan 

---

## 🛠️ Tech Used
- Python 3
- Flask
- AWS EC2
- Ubuntu
- systemd
- GitHub

---

## 📦 Installationpip3 install -r requirements.txt
python3 app.py

---

## 🌍 Deployment Guide (Short)
1. Launch EC2 Ubuntu instance  
2. Install Python + pip  
3. Clone/upload the project  
4. Install dependencies  
5. Create systemd service  
6. Enable + start service  
7. Open port 5000 in Security Group  
8. Access: http://3.111.35.183:5000  

---

## 📄 Licence
This project is open-source.



