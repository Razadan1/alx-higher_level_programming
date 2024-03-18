#!/usr/bin/python3
def multiple_returns(sentence):
    for item in sentence:
        if sentence == '':
            return None
        else:
            return (len(sentence), item[0])