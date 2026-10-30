# MLOps Tool Setup & UAT Dry Run (Lab Internal POE)

**Student Name:** Abhi Trambadiya  
**Roll No:** A36 (Division A, Roll No. 36)  
**PRN:** 2324000344  
**Course:** Lab MLDevOps (Semester 07)  
**Repository:** [github.com/abhitrambadiya/Lab-Internal-POE-MLOps](https://github.com/abhitrambadiya/Lab-Internal-POE-MLOps)  

---

## 1. Executive Summary & Purpose

The objective of this MLOps Internal POE is to design, implement, and validate an end-to-end **Continuous Integration, Containerization, and Monitoring** workflow simulating a **UAT (User Acceptance Testing) Environment Dry Run**.

Modern machine learning systems fail not only because of code bugs, but due to **environment drift**, **silent dependency rot**, and **unmonitored data distribution drift**. This project sets up an automated pipeline verifying:
1. **Developer Environment & Git VCS**: VSCode workspace structured and version-controlled with Git.
2. **Automated Testing (Pytest)**: Unit test suite for application behavior and feature calculation logic.
3. **Containerization (Docker)**: Packaging the Python application into a lightweight, isolated Alpine container.
4. **CI/CD Automation (Jenkins)**: Declarative pipeline automating checkout, testing, packaging, and validation stages.
5. **Continuous Model & Data Monitoring (Evidently AI)**: Real-time drift detection comparing reference baseline data against incoming production/UAT inference data.

---

## 2. Project Architecture & Structure

```
Lab Internal POE/
├── hello.py                     # Core application with logic & feature scoring
├── Dockerfile                   # Lightweight Python 3.11-alpine container definition
├── Jenkinsfile                  # CI/CD declarative pipeline (6 stages)
├── requirements.txt             # Python project dependencies
├── tests/
│   └── test_hello.py            # Pytest test cases (greeting & scoring logic)
├── monitoring/
│   ├── monitor.py               # Evidently AI drift detection & reporting script
│   └── reports/
│       ├── evidently_drift_report.html
│       └── evidently_drift_report.json
├── output/
│   └── Lab_Internal_POE_Report.pdf  # Comprehensive execution & output report
└── README.md                    # Project documentation
```

---

## 3. MLOps Tools Implemented

| Tool Name | Category | Purpose in Lifecycle |
| :--- | :--- | :--- |
| **VSCode + Git** | Source Control & IDE | Local workspace setup, structured commits, and GitHub repository hosting. |
| **Pytest** | Test Automation | Verifying data functions, edge cases, and preventing regressions before build. |
| **Docker** | Containerization | Packaging lightweight `python:3.11-alpine` container ensuring environmental parity. |
| **Jenkins** | CI/CD Automation | Orchestrating multi-stage pipeline from pull to test, build, and monitoring. |
| **Evidently AI** | Model Monitoring | Detecting feature drift and data quality degradation between reference & production data. |

---

## 4. Step-by-Step Execution & Commands

### Step 1: Run the Application Locally
```bash
python3 hello.py
```
*Output:*
```
Hello, DevOps Engineer! Welcome to MLOps Lab Internal POE.
Sample Feature Calculation Score: 11.15
```

### Step 2: Run Pytest Automation Suite
```bash
pytest tests/ -v
```
*Outcome:* 2 passed test cases verifying greeting formatting and feature calculations.

### Step 3: Build & Run Docker Container
```bash
# Pull lightweight base image
docker pull python:3.11-alpine

# Build container image
docker build -t mlops-hello-poe:latest .

# Execute container UAT dry run
docker run --rm mlops-hello-poe:latest

# Run pytest inside container
docker run --rm mlops-hello-poe:latest pytest tests/ -v
```

### Step 4: Run Evidently AI Monitoring Suite
```bash
python3 monitoring/monitor.py
```
*Generates:*
- `monitoring/reports/evidently_drift_report.html` (Interactive visual dashboard)
- `monitoring/reports/evidently_drift_report.json` (Automated drift metric payload)

### Step 5: Jenkins Pipeline Execution
The included `Jenkinsfile` runs 6 declarative stages:
1. **Checkout Source**: Pulls repository branch from GitHub.
2. **Environment & Tool Verification**: Validates Docker, Python, and Git presence.
3. **Pytest Automation**: Executes test suite.
4. **Docker Build & Package**: Assembles lightweight container.
5. **Docker Dry Run Execution**: Runs container to verify zero runtime failures.
6. **Evidently Model Monitoring**: Executes drift validation suite.

---

## 5. Summary Report of Installation & Tool Status

| Tool Name | Command(s) Used | Installation / Run Status |
| :--- | :--- | :--- |
| **VSCode & Git** | `git init`, `git add .`, `git commit` | **Successful** (Configured & active) |
| **Pytest** | `pytest tests/ -v` | **Successful** (2/2 test cases passed) |
| **Docker** | `docker pull python:3.11-alpine`, `docker build`, `docker run` | **Successful** (Container executed in UAT dry run) |
| **Jenkins** | `Jenkinsfile` declarative pipeline definition | **Successful** (Configured for SCM webhook triggers) |
| **Evidently AI** | `python3 monitoring/monitor.py` | **Successful** (Drift & Data Quality report generated) |

---

## 6. Outcomes & Real-World Value

- **Environmental Reproducibility**: Using lightweight Alpine containers eliminates "it worked on my machine" issues across developer machines and UAT servers.
- **Fail-Fast Quality Gates**: Pytest catches faulty transformations and broken API logic before artifacts reach container packaging.
- **Proactive Observability**: Evidently AI flags feature drift and statistical variance before machine learning model accuracy degrades in production.
- **Audit-Ready Pipeline**: Automated Jenkins declarative pipelines provide immutable build artifacts and execution logs for compliance.
