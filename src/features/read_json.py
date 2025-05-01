import json
import os


def read_json():
    data = []
    if os.path.exists("db.json"):
        with open("db.json", "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    return data