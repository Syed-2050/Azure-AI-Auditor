#!/usr/bin/env python3

import json
import subprocess
import requests
from datetime import datetime

MODEL_NAME = "qwen2.5:1.5b"

def run_az(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return []
    return json.loads(result.stdout) if result.stdout.strip() else []

def get_subscription_id():
    result = subprocess.run(
        ["az", "account", "show", "--query", "id", "-o", "tsv"],
        capture_output=True,
        text=True
    )
    sub_id = result.stdout.strip()
    if not sub_id:
        print("Not logged in to Azure. Run: az login --use-device-code")
        exit(1)
    return sub_id

def get_azure_data():
    print("Scanning Azure resources...")

    data = {
        "resource_groups": run_az(["az", "group", "list", "-o", "json"]),
        "virtual_machines": run_az(["az", "vm", "list", "-o", "json"]),
        "storage_accounts": run_az(["az", "storage", "account", "list", "-o", "json"]),
        "network_security_groups": run_az(["az", "network", "nsg", "list", "-o", "json"]),
        "virtual_networks": run_az(["az", "network", "vnet", "list", "-o", "json"])
    }

    return data

def ask_ai(data):
    prompt = f"""
You are an Azure cloud security and cost optimization assistant.

Analyze this Azure infrastructure data and provide:
1. Security observations
2. Cost optimization suggestions
3. Architecture observations
4. Top 5 recommendations

Azure Data:
{json.dumps(data, indent=2)}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )

    result = response.json()
    return result.get("response", str(result))

def save_report(data, ai_report):
    filename = "reports/azure-audit-report.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""# Azure AI Infrastructure Audit Report

Generated: {timestamp}

## Summary

| Resource | Count |
|---|---|
| Resource Groups | {len(data["resource_groups"])} |
| Virtual Machines | {len(data["virtual_machines"])} |
| Storage Accounts | {len(data["storage_accounts"])} |
| Network Security Groups | {len(data["network_security_groups"])} |
| Virtual Networks | {len(data["virtual_networks"])} |

## AI Analysis

{ai_report}
"""

    with open(filename, "w") as f:
        f.write(content)

    print(f"Report saved to {filename}")

def main():
    print("AZURE AI RESOURCE AUDITOR")
    print("=========================")

    sub_id = get_subscription_id()
    print(f"Connected subscription: {sub_id}")

    data = get_azure_data()
    ai_report = ask_ai(data)
    save_report(data, ai_report)

    print("\nAI Report Preview:\n")
    print(ai_report[:1000])

if __name__ == "__main__":
    main()
