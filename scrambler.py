#!/bin/python3.8
import json
import random
# from operator import itemgetter
cardlist = []

nice = open('info.json')
cardlist = json.load(nice)
scrambled = {}


def scramble(cardlist):
    ramdomlist = {}
    for j in cardlist:
        # ramdomlist[j] = {}
        ramdomlist[j] = random.random()
    ramdomsortedlist = sorted(ramdomlist.items(), key=lambda kv: kv[1])

    for k in range(len(cardlist)):
        scrambled[k] = cardlist[ramdomsortedlist[k][0]]
    print(scrambled)


scramble(cardlist)
