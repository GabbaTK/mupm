import os
import time
import json

if not os.path.exists(r".\cache"):
    with open(r".\cache", "w") as c: c.write("{}")

def add(data: dict, ttl=-1):
    with open(r".\cache", "r") as cache:
        parsed = json.loads("".join(cache.readlines()))

        for key, val in data.items():
            parsed[key] = {"ttl": int(time.time()) + ttl, "dat": val}

    with open(r".\cache", "w") as cache:
        cache.write(str(parsed).replace("'", '"'))

def delete(data: list):
    with open(r".\cache", "r") as cache:
        parsed = json.loads("".join(cache.readlines()))

        for key in data:
            if key in parsed:
                del parsed[key]

    with open(r".\cache", "w") as cache:
        cache.write(str(parsed).replace("'", '"'))

def empty():
    with open(r".\cache", "w") as c: c.write("{}")

def get(data_id: str):
    with open(r".\cache", "r") as cache:
        parsed = json.loads("".join(cache.readlines()))

        if data_id in parsed:
            return parsed[data_id]["dat"]
        
        return None

def expire():
    with open(r".\cache", "r") as cache:
        parsed = json.loads("".join(cache.readlines()))
        keys = list(parsed.keys())

        for key in keys:
            if parsed[key]["ttl"] < 0: continue
            if parsed[key]["ttl"] < time.time():
                del parsed[key]

    with open(r".\cache", "w") as cache:
        cache.write(str(parsed).replace("'", '"'))
