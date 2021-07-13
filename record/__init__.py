import json

FILE_NAME = "data/records"

def save(level: int) -> None:
    records = {"level": level}
    with open(FILE_NAME, "w") as f:
        f.write(json.dumps(records))

def read() -> dict:
    with open(FILE_NAME, "r") as f:
        data = f.read()
    return json.loads(data)
