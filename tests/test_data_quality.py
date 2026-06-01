from validation.quality_checks import validate_issue_record


def test_valid_issue_record():
    record = {
        "issue_id": "1001",
        "key": "PROJ-101",
        "status": "Done",
    }
    assert validate_issue_record(record) == []


def test_missing_issue_id():
    record = {
        "key": "PROJ-102",
        "status": "In Progress",
    }
    assert "Missing issue_id" in validate_issue_record(record)
