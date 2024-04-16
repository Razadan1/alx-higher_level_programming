#!/usr/bin/python3
""" This function writes an Object to a text file using a Json representation"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file using Json"""
    json_obj = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as writeJson:
        writeJson.write(json_obj)
