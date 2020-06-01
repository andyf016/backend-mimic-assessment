#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "???"

import random
import sys
from collections import defaultdict

def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    mimic_dict = defaultdict(list)
    with open(filename) as book:                            #Open file with context management 
        first_word = book.readline().split()                #Split the first line into a list 
        mimic_dict.setdefault('', first_word[0])            #Set the 'seed' key and value as described in readme
    with open(filename) as book:
        for line in book.readlines():                       #Loop over the lines and split them into lists of words
            words = line.split()                             
            for i, word in enumerate(words):                #Enumerate each word for slicing
                try:
                    next_word = words[i+1]                  #find the "next word" for the value
                    mimic_dict.setdefault(word, [])         #Use setdefault() to define a key
                    mimic_dict[word].append(next_word)      #Use append() to add the 'next word' to the lis of values
                except:
                    break
    final = dict(mimic_dict)
    return final

#print(create_mimic_dict('imdev.txt'))


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    lst = []                                #Define an empty list to contain the random words
    keys = list(mimic_dict.keys())          #Create a list of keys from the mimic_dict                
    word = start_word                       #First assignment of 'word' variable which will be used to define the current key in the mimic dict 
    print(start_word)
    for i in range(200):
        word_value = random.choice(mimic_dict.get(word))    #randomly select a value from the list of values of the current 'word' key
        lst.append(word_value)                              #add the random word to the list of words
        word = random.choice(keys)                          #randomly choose a new 'word' key
    final = ' '.join(lst)                                   #join the list of words into a string
    print(final)                                            #print the string 
    return final



# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
