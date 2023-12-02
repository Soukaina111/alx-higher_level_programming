#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple1 = (0, None)
    else:
        tuple1 = (len(sentence), sentence[:1])
    return (tuple1)
