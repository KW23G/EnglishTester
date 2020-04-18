#  from en_words.txt -> en_to_de.json + de_to_en.json

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

if "en_to_de.json" not in os.listdir():
    os.system("touch en_to_de.json")

if "de_to_en.json" not in os.listdir():
    os.system("touch de_to_en.json")

###################
# en - de:

big_dict1 = {word: {"translation": trans(word), "level": 3} for word in all_words}

l = int(len(big_dict1) / 4)

big_list1 = [create_dict(list(big_dict1.keys())[0:l], list(big_dict1.values())[0:l]), create_dict(list(big_dict1.keys())[l:(2*l)], list(big_dict1.values())[l:(2*l)]),
             create_dict(list(big_dict1.keys())[(2*l):(3*l)], list(big_dict1.values())[(2*l):(3*l)]), create_dict(list(big_dict1.keys())[(3*l):], list(big_dict1.values())[(3*l):])]

with open("en_to_de.json", "w") as f:
    json.dump(big_list1, f)

###################
# de - en:

big_dict2 = {trans(word): {"translation": word, "level": 3} for word in all_words}

l = int(len(big_dict2) / 4)

big_list2 = [create_dict(list(big_dict2.keys())[0:l], list(big_dict2.values())[0:l]), create_dict(list(big_dict2.keys())[l:(2*l)], list(big_dict2.values())[l:(2*l)]),
             create_dict(list(big_dict2.keys())[(2*l):(3*l)], list(big_dict2.values())[(2*l):(3*l)]), create_dict(list(big_dict2.keys())[(3*l):], list(big_dict2.values())[(3*l):])]

with open("de_to_en.json", "w") as f:
    json.dump(big_list2, f)
