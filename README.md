# Azure AI Resource Auditor

AI-powered Azure infrastructure auditing tool built using Python, Azure CLI, and Ollama.

This project scans Azure resources, collects infrastructure data, and uses a local AI model to generate security, architecture, and cost optimization recommendations.

---

## Features

### Azure Resource Discovery

* Resource Groups
* Virtual Machines
* Storage Accounts
* Network Security Groups (NSGs)
* Virtual Networks (VNets)

### AI-Powered Analysis

* Security observations
* Cost optimization suggestions
* Architecture review
* Best-practice recommendations
* Risk assessment

### Report Generation

* Markdown audit reports
* Infrastructure summary
* AI-generated recommendations

---

## Architecture

Azure Subscription

↓

Azure CLI

↓

Python Automation

↓

Ollama Local AI (Qwen2.5)

↓

Azure Audit Report

---

## Technologies Used

* Python
* Azure CLI
* Ollama
* Qwen2.5 Local LLM
* Git
* GitHub
* Linux (Ubuntu)

---

## Project Structure

azure-ai-auditor/

├── main.py

├── requirements.txt

├── README.md

├── .gitignore

├── reports/

│   ├── sample-report.md

│   └── azure-audit-report.md

└── venv/

---

## Sample Capabilities

### Security Review

* Reviews Azure resource configuration
* Highlights missing tags
* Identifies potential security gaps
* Reviews NSG configuration

### Cost Optimization

* Detects underutilized infrastructure
* Highlights unnecessary resources
* Recommends cost-saving opportunities

### Architecture Review

* Reviews resource organization
* Examines Azure deployment structure
* Suggests best practices

---

## How To Run

### Login to Azure

```bash
az login --use-device-code
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Ollama

```bash
ollama run qwen2.5:1.5b
```

### Run Auditor

```bash
python main.py
```

---

## Example Output

* Azure infrastructure inventory
* Security observations
* Cost optimization suggestions
* Architecture recommendations
* Markdown audit report

Generated report:

```text
reports/azure-audit-report.md
```

---

## Skills Demonstrated

* Microsoft Azure
* Cloud Security
* Cloud Governance
* Cost Optimization
* Python Automation
* Infrastructure Auditing
* AI Integration
* Linux Administration
* Git & GitHub

---

## Author

Syed Arif Ali - Cloud Engineer

Email: Syedarif1907@gmail.com
LinkedIn: www.linkedin.com/in/syed-arif-a-a13782407
GitHub: github.com/Syed-2050
