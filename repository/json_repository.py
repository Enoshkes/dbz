import json

from model.warrior import Warrior


def read_json(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(e)
        return []

def convert_from_json_to_warrior(json):
    return Warrior(
        uid=json["id"],
        name=json["name"],
        ki=json["ki"],
        max_ki=json["maxKi"],
        affiliation=["affiliation"],
        description=["affiliation"],
        gender=json["gender"],
        race=json["race"]
    )
