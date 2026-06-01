import requests


def fetch_jira_issues(base_url, token, project_key):
    url = f"{base_url}/rest/api/2/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"jql": f"project={project_key}", "maxResults": 100}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    issues = response.json().get("issues", [])

    return [
        {
            "issue_id": issue.get("id"),
            "key": issue.get("key"),
            "summary": issue.get("fields", {}).get("summary"),
            "status": issue.get("fields", {}).get("status", {}).get("name"),
            "assignee": issue.get("fields", {}).get("assignee", {}).get("displayName")
            if issue.get("fields", {}).get("assignee")
            else None,
        }
        for issue in issues
    ]
