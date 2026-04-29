def transform(record):
    if record["age"] < 0:
        return None
    record["name"] = record["name"].upper()
    return record