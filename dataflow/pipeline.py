def transform_record(record):
    return {
        "issue_id": record.get("issue_id"),
        "key": record.get("key"),
        "summary": record.get("summary", "").strip(),
        "status": record.get("status", "Unknown"),
        "assignee": record.get("assignee"),
        "processed_at": record.get("processed_at"),
    }


def filter_valid_records(record):
    return record.get("issue_id") is not None and record.get("key") is not None
