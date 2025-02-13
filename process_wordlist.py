#!/usr/bin/env python3

from typing import List

# Empty List
word_list_by_length = {}

# Process, bucketing by length.
with open('wordlist.txt', 'r') as f:
    line:str = f.readline()
    while line:
        word = line.strip().lower()
        word_length:int = len(word)
        if word_length not in word_list_by_length.keys():
            word_list_by_length[word_length] = []
        word_list_by_length[word_length].append(word)
        line = f.readline()

lengths:list[int] = sorted(word_list_by_length.keys(), reverse=True)
output:str = 'word_list:list[str] = ['
first:bool = True
for length in lengths:
    words = word_list_by_length[length]
    for word in words:
        if first:
            first = False
        else:
            output += ','
        output += "'{0}'".format(word)
output += ']'
print(output)
