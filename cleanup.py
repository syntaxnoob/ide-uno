#!/bin/python3.8
import json

cardlist = {}

with open('cards.json', 'r') as f:
    cardlist = json.loads(f).content.decode('utf-8')
print(cardlist)
