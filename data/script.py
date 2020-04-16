#  from en_words.txt -> data.json

#################################################

import json
import os
from translate import Translator
translator = Translator(to_lang="de")


def trans(en_word):
    return translator.translate(en_word)


def create_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

#################################################


with open("en_words.txt", "r") as f:
    all_words = f.read().split("\n")

all_words = all_words[100:]

if "data.json" not in os.listdir():
    os.system("touch data.json")

big_dict = {word: {"translation": trans(word), "level": 3} for word in all_words}

l = int(len(big_dict) / 4)

big_list = [create_dict(list(big_dict.keys())[0:l], list(big_dict.values())[0:l]), create_dict(list(big_dict.keys())[l:(2*l)], list(big_dict.values())[l:(2*l)]),
            create_dict(list(big_dict.keys())[(2*l):(3*l)], list(big_dict.values())[(2*l):(3*l)]), create_dict(list(big_dict.keys())[(3*l):], list(big_dict.values())[(3*l):])]

with open("data.json", "w") as f:
    json.dump(big_list, f)
