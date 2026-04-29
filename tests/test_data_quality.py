def validate(record):
    if record["age"] < 0:
        return False
    if "@" not in record["email"]:
        return False
    return True

def test_valid_data():
    assert validate({"age":25,"email":"a@gmail.com"}) == True

def test_invalid_data():
    assert validate({"age":-1,"email":"abc"}) == False