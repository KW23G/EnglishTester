#  from en_words.txt -> data.json

#################################################

import json
import os
from translate import Translator
translator = Translator(to_lang="de")


def trans(en_word):
    return translator.translate(en_word)

#################################################


with open("en_words.txt", "r") as f:
    all_words = f.read().split("\n")

all_words = all_words[100:]

if "data.json" not in os.listdir():
    os.system("touch data.json")

big_dict = {word: {"translation": trans(word), "level": 3} for word in all_words}

with open("data.json", "w") as f:
    json.dump(big_dict, f)
