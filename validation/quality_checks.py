def validate_issue_record(record):
    errors = []

    if not record.get("issue_id"):
        errors.append("Missing issue_id")

    if not record.get("key"):
        errors.append("Missing issue key")

    if not record.get("status"):
        errors.append("Missing status")

    return errors
