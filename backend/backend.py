import json

# helper functions:


def read(file):
    with open(f"../data/{file}", "r") as f:
        return json.load(f)


def write(content, file):
    with open(f"../data/{file}", "w") as f:
        return json.dump(content, f)


def create_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

###########################


def get_word(lan):  # lan = de / en
    pass


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
