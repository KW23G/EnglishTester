import json

# helper functions:


def read(file):
    with open(f"data/{file}", "r") as f:
        return json.load(f)


def create_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

###########################


def get_word(lan):  # lan = de / en
    pass


def check_translation(en, de):
    file = read("en_to_de.json")

    for x in range(4):
        if en in file[x]:
            if file[x][en]["translation"] == de:
                file[x][en]["level"] -= 1
                return True

            else:
                file[x][en]["level"] += 1
                return False
