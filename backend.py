import json

# helper functions:


def read():
    with open("data/data.json", "r") as f:
        return json.load(f)

###########################


def get_word(lan):  # lan = de / en
    pass


def check_translation(en, de):
    file = read()

    for x in range(4):
        if en in file[x]:
            if file[x][en]["translation"] == de:
                file[x][en]["level"] -= 1
                return True

            else:
                file[x][en]["level"] += 1
                return False
