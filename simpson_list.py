#!/usr/bin/python3

"""
Automate with Python
Panda library reading content from the webpage and storing as a list in a variable.
"""
import pandas as pd

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

print(len(simpsons))
print(simpsons[1])

