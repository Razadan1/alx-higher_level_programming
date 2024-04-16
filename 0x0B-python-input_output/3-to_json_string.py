#!/usr/bin/python3
""" This function returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """ Returns JSON of an object """
    return json.dumps(my_obj)
