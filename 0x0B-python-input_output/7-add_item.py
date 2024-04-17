#!/usr/bin/python3
""" A script that adds all arguements to a python list"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg = sys.argv
namedFile = "add_item.json"
with open(namedFile, mode="a", encoding="utf-8") as filename:
    d_list = []
    d_list.extend(arg[1:])
    save_to_json_file(d_list, namedFile)
    load_from_json_file(namedFile)
