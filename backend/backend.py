import json
import random

# helper functions:


def read(file):
    with open(f"data/{file}", "r") as f:
        return json.load(f)


def write(content, file):
    with open(f"data/{file}", "w") as f:
        json.dump(content, f)


def create_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

###########################


def get_word(lan):  # lan = de / en
    if lan != "en" or lan != "de":
        raise Exception()

    json_file = read("en_to_de.json") if lan == "en" else read("de_to_en.json")

    prozent = random.randint(1, 100)

    if prozent <= 50:  # 50 %
        section = json_file[0]
    elif prozent <= 80:  # 30 %
        section = json_file[1]
    elif prozent <= 93:  # 13 %
        section = json_file[2]
    else:  # 7 %
        section = json_file[3]


def check_en_to_de(en, de):
    d = read("en_to_de.json")

    for x in range(4):
        if en in d[x]:
            if d[x][en]["translation"] == de:
                d[x][en]["level"] -= 1
                write(d, "en_to_de.json")
                return True

            else:
                d[x][en]["level"] += 1
                write(d, "en_to_de.json")
                return False

    d[x][en]["level"] += 1
    write(d, "en_to_de.json")
    return False


def check_de_to_en(de, en):
    d = read("de_to_en.json")

    for x in range(4):
        if de in d[x]:
            if d[x][de]["translation"] == en:
                d[x][de]["level"] -= 1
                write(d, "de_to_en.json")
                return True

            else:
                d[x][de]["level"] += 1
                write(d, "de_to_en.json")
                return False

    d[x][de]["level"] += 1
    write(d, "de_to_en.json")
    return False
