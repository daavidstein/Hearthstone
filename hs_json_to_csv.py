#!/usr/bin/env python

"""This script generates a CSV file from the Hearthstone JSON API,
including only those fields in the list NEEDED_FIELDS"""
import csv
import json
import requests


CARDDATA = requests.get("https://api.hearthstonejson.com/v1/25770/enUS/cards.json")
CARDS = json.loads(CARDDATA.text)


MYLIST = []
UNNEEDED_FIELDS = ["faction", "artist", "flavor", "howToEarn", "howToEarnGolden", \
        "targetingArrowText"]
NEEDED_FIELDS = ["dbfId", "cardClass", "collectible", "cost", "name", "mechanics", "rarity", \
"set", "text", "type", "playRequirements", "referencedTags", "attack", "health", "race", \
"hideStats", "multiClassGroup", "classes", "collectionText"]

with open('cards.csv', 'w') as csvfile:
    MYWRITER = csv.writer(csvfile, delimiter=',', quotechar='`', quoting=csv.QUOTE_MINIMAL)
    MYWRITER.writerow(NEEDED_FIELDS) #add csv header
    for card in CARDS:
        for field in NEEDED_FIELDS:
            if field in list(card.keys()):
                MYLIST.append(card[field])
            else:
                MYLIST.append("")
        MYWRITER.writerow(MYLIST)
        MYLIST = []
