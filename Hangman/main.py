import pandas as pd
import random

# We going to extract the words from a JSON file.
words = pd.read_json("https://www.randomlists.com/data/words.json")


def getValidWord(words) -> str:
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
