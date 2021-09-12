import json
#from os import EX_PROTOCOL

FILE_NAME = "data/records.json"


# 儲存遊戲紀錄，出錯則回傳錯誤。 若沒有錯誤回傳None
def save(level: int) -> Exception:
    records = {"level": level}
    try:
        with open(FILE_NAME, "w") as f:
            f.write(json.dumps(records))
    except Exception as err:
        print("error: cannot save\n", err)
        return err
    return None

# 讀取遊戲紀錄，出錯則回傳空dict
def read() -> dict:
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read()
    except Exception as err:
        print("error: cannot save\n", err)
        return dict()
    return json.loads(data)
