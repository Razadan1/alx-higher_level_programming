#!/usr/bin/python3
""" A function that creates an object from Json file """
import json


def load_from_json_file(filename):
    """ Creates an object from json"""
    with open(filename, mode="r", encoding="utf-8") as jsonfile:
        obj_from_json = json.load(readFile)
    return obj_from_json