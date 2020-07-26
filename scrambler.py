#!/bin/python3.8
import json
import random

cardlist = {}
ram1 = {}
ram2 = {}


nice = open('info.json')
cardlist = json.load(nice)


def scramble():
    for i in range(50):
        for j in cardlist:
