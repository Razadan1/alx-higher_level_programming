#!/usr/bin/python3
""" A script that adds all arguements to a python list"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

namedFile = "add_item.json"
try:
    d_list = load_from_json_file(namedFile)
except FileNotFoundError:
    d_list = []

for i in range(1, len(sys.argv)):
    d_list.append(sys.argv[i])

save_to_json_file(d_list, namedFile)
