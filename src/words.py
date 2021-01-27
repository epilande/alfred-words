#!/usr/bin/python3

import sys
import os
import argparse
import json
dirname = os.path.dirname(__file__)
sys.path.append(os.path.join(dirname, "lib"))

from lib import requests

parser = argparse.ArgumentParser()
parser.add_argument('--queryType', default='syn')
args = parser.parse_args()
queryType = args.queryType
word = os.environ['word']

DEBUG = False


def fetchWords():
    response = requests.get(
        f"https://tuna.thesaurus.com/pageData/{word}",
        headers={
            "Content-Type": "application/json",
        }
    )

    json_response = response.json()
    definitionData = json_response.get('data', {}).get('definitionData')
    definitions = definitionData.get('definitions')[0]
    definition = definitions.get('definition')
    synonyms = list(map(lambda x: x['term'], definitions['synonyms']))
    antonyms = list(map(lambda x: x['term'], definitions['antonyms']))

    if DEBUG:
        # print(json.dumps(json_response, indent=4))
        print(f"https://tuna.thesaurus.com/pageData/{word}")
        print('definitions: ', definitions)
        print('definition: ', definition)
        print('synonyms: ', synonyms)
        print('antonyms: ', antonyms)

    items = list(map(lambda item: {
        "title": item,
        "arg": item
    }, antonyms if queryType == "ant" else synonyms))

    definitionItem = [{
        "title": definition,
        "subtitle": f"📖 definition of \"{word}\"",
        "arg": definition
    }]

    return print(json.dumps({'items': definitionItem + items}))


if __name__ == '__main__':
    fetchWords()
