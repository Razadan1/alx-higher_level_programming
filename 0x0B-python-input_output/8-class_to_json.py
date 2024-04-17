#!/usr/bin/python3
""" A function that returns the dictionary description
with simple data structure"""


def class_to_json(obj):
    if isinstance(obj, (int, str, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(i) for i in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        return class_to_json(obj.__dict__)
    else:
        raise TypeError(f"Object of type {type(obj)}is not Json serialized")
