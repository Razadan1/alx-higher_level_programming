#!/usr/bin/python3
""" This function writes an Object to a text file using a Json"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file using Json"""
    with open(filename, mode="w", encoding="utf-8") as writeJson:
        writeJson.write(json.dumps(my_obj))
