import json

# Geel Groen Rood Blauw

cards = {}
testnumber = 0
ram = 0
currentcolor = 0


colorlist = ['Geel', 'Groen', 'Rood', 'Blauw']
boostlist = ['plus2', 'ronddraaien', 'beurtoverslaan']

for i in range(0, (108), 2):

    cards[i] = {}
    cards[i+1] = {}
    if (ram < 12):
        cards[i]['cardnr'] = ram
        cards[i+1]['cardnr'] = ram
        if (14 > ram > 9):
            cards[i]['cardboost'] = boostlist[ram-10]
            cards[i+1]['cardboost'] = boostlist[ram-10]

    if (ram >= 13):
        break
    if (ram < 13):
        if currentcolor == 0:
            cards[i]['cardcolor'] = colorlist[currentcolor]
            cards[i + 1]['cardcolor'] = colorlist[currentcolor]

            currentcolor = currentcolor + 1
        elif currentcolor == 1:
            cards[i]['cardcolor'] = colorlist[currentcolor]
            cards[i + 1]['cardcolor'] = colorlist[currentcolor]

            currentcolor = currentcolor + 1
        elif currentcolor == 2:
            cards[i]['cardcolor'] = colorlist[currentcolor]
            cards[i + 1]['cardcolor'] = colorlist[currentcolor]

            currentcolor = currentcolor + 1
        elif currentcolor == 3:
            cards[i]['cardcolor'] = colorlist[currentcolor]
            cards[i + 1]['cardcolor'] = colorlist[currentcolor]

            ram = ram + 1
            currentcolor = 0
        else:
            print('groot probleem')
print(cards)

for test in cards:
    try:
        if (cards[test]['cardcolor'] == 'Blauw' and cards[test]['cardnr'] < 10):
            testnumber = testnumber + 1
            print(cards[test])
    except KeyError as e:
        print(e)

print(testnumber)