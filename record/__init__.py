import json
import logging

FILE_NAME = "data/records.json"


def save(**kwargs) -> Exception:
    '''
    儲存遊戲紀錄，出錯則回傳錯誤。 若沒有錯誤回傳None
    範利用法：save(level=10, saver="test", game="sokoban pygame")
    '''
    records = kwargs
    try:
        with open(FILE_NAME, "w") as f:
            f.write(json.dumps(records))
    except Exception as err:
        logging.error("cannot save data", err)
        return err
    return None

def read() -> dict:
    '''讀取遊戲紀錄，出錯則回傳空dict'''
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read()
    except Exception as err:
        logging.error("cannot read data", err)
        return dict()
    return json.loads(data)

if __name__ == "__main__":
    save(level=10, saver="test", game="sokoban pygame")
