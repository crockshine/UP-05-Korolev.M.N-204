import json
import os


def append_json(track_info: dict):
    data = []
    if os.path.exists("db.json"):
        with open("db.json", "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    data.append({'track_id':len(data), **track_info})

    with open("db.json", "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                default=str,
                ensure_ascii=False
            )