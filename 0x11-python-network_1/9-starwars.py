#!/usr/bin/python3
""" Script that takes in a string and sends a search request to the Star Wars
    API
"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get('https://swapi.co/api/people/?search={}'
                       .format(argv[1]))
    req_json = req.json()
    print('Number of results: {}'.format(req_json.get('count')))
    for res in req_json.get('results'):
        print(res.get('name'))
