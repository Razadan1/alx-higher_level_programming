#!/usr/bin/python3
""" This function returns the object represented by a Json"""
import json


def from_json_string(my_str):
    """ Returns object represented by Json """
    return json.loads(my_str)
