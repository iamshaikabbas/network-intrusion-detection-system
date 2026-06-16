# network-intrusion-detection-system
Real-time DDoS detection system built with Python, Flask, Streamlit, Random Forest, Isolation Forest, and network traffic analysis for detecting malicious traffic and monitoring attack activity.
# 🛡️ Real-Time DDoS Detection System

## Overview

This project is a real-time Distributed Denial-of-Service (DDoS) detection system that combines machine learning, anomaly detection, rule-based analysis, and live monitoring to identify suspicious network traffic.

The system processes incoming traffic data, extracts real-time traffic features, evaluates network behavior using trained machine learning models, and displays attack status through an interactive dashboard.

The goal of this project is to demonstrate how cybersecurity analytics and machine learning can be combined to improve network threat detection and monitoring.

---

## Project Objective

The primary objective of this project is to detect potential DDoS attacks in real time by analyzing network traffic characteristics and identifying abnormal patterns.

The system aims to:

- Monitor incoming network traffic.
- Detect attack behavior using machine learning.
- Identify anomalies in traffic patterns.
- Generate real-time attack alerts.
- Visualize network activity through a live dashboard.

---

## System Architecture

```text
Traffic Simulation
        ↓
Flask API
        ↓
Feature Extraction Engine
        ↓
Machine Learning Models
        ↓
Attack Detection Logic
        ↓
Real-Time Dashboard
```

---

## Key Features

### Real-Time Traffic Monitoring

- Continuously monitors incoming traffic.
- Calculates live traffic metrics.
- Tracks packet rates and network behavior.

### Machine Learning-Based Detection

The system uses:

#### Random Forest Classifier

- Detects known attack patterns.
- Classifies traffic as normal or malicious.

#### Isolation Forest

- Detects anomalous traffic behavior.
- Identifies unknown attack patterns.

### Rule-Based Detection

Additional security rules are used to detect:

- High packet rates
- Abnormally large packet sizes
- Suspicious traffic spikes

This hybrid approach improves detection accuracy.

### Live Dashboard

A Streamlit dashboard provides:

- Live traffic visualization
- Attack status monitoring
- Real-time alerts
- Traffic rate analysis

### Traffic Simulation

A built-in attack simulator generates both:

- Normal traffic
- Attack traffic

This allows testing and validation of the detection system.

---

## Technologies Used

### Programming Language

- Python

### Backend

- Flask

### Dashboard

- Streamlit

### Machine Learning

- Random Forest
- Isolation Forest

### Data Processing

- Pandas
- NumPy

### Networking

- HTTP Requests
- Real-Time Traffic Analysis

---

## Detection Workflow

### Step 1: Traffic Generation

Traffic data is generated through the simulator and sent to the Flask API.

### Step 2: Feature Extraction

The real-time engine calculates:

- Traffic Rate
- Average Packet Size
- Average TTL

### Step 3: Machine Learning Prediction

Traffic is evaluated using:

- Random Forest Model
- Isolation Forest Model

### Step 4: Rule Validation

Additional checks include:

- Traffic rate thresholds
- Packet size limits

### Step 5: Attack Classification

Traffic is classified as:

- Normal
- Attack

### Step 6: Dashboard Visualization

Results are displayed in real time through the Streamlit dashboard.

---

## Project Structure

```text
real-time-ddos-detection-system/
│
├── app.py
├── attack_simulator.py
├── dashboard.py
├── realtime_engine.py
├── models/
│   ├── rf_model.pkl
│   └── iso_model.pkl
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### Clone Repository

```bash
git clone https://github.com/iamshaikabbas/real-time-ddos-detection-system.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Flask Server

```bash
python app.py
```

### Launch Dashboard

```bash
streamlit run dashboard.py
```

### Run Traffic Simulation

```bash
python attack_simulator.py
```

---

## Skills Demonstrated

- Cybersecurity Analytics
- Machine Learning
- Anomaly Detection
- Network Traffic Analysis
- Threat Detection
- Flask API Development
- Streamlit Dashboard Development
- Real-Time Data Processing
- Python Programming
- Security Monitoring

---

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Building real-time cybersecurity applications.
- Implementing machine learning-based threat detection.
- Detecting anomalous network behavior.
- Designing live monitoring dashboards.
- Integrating multiple detection techniques into a single system.

---

## Future Improvements

- Deep Learning-based detection models
- Automated alert notifications
- SIEM integration
- Threat intelligence feeds
- Cloud deployment
- Multi-class attack classification

---

## About Me

### Shaik Abbas

Aspiring Data Analyst and Cybersecurity Enthusiast passionate about data analytics, machine learning, business intelligence, and network security.

- GitHub: https://github.com/iamshaikabbas
- LinkedIn: https://www.linkedin.com/in/shaik-abbas-a5a723287/

---

## Disclaimer

This project is intended solely for educational and research purposes. It focuses on detecting and analyzing DDoS attack patterns and does not provide instructions for conducting attacks.
