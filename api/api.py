# URL - https://app.prefect.cloud/account/8ff8f613-92c4-44ce-b811-f9956023e78d/workspace/04d8fca9-df2e-40c8-ae4f-a3733114c475/dashboard

# Ref - https://app.prefect.cloud/api/docs

import requests

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "***************************"  # Your Prefect Cloud API key
ACCOUNT_ID = "***************************"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "***************************" # Your Prefect Cloud Workspace ID
DEPLOYMENT_ID = "***************************" # Your Deployment ID

# Correct API URL to list flow runs
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/flows/filter"

# Data to filter artifacts
data = {
  "limit": 10,
  "sort": "CREATED_DESC"
}

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request
response = requests.post(PREFECT_API_URL, headers=headers, json=data)
print(response)

# Check the response status
if response.status_code != 200:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
else:
    artifacts = response.json()
    # print(artifacts)
    for artifact in artifacts:
        print(artifact)
