#!/usr/bin/env python3
# generate_passphrase.py
# generate 3 numbers between 1 and 20
# then choose phrases from the trek list
# can also use the harry potter list or others
# based on the eff dice generated passphrase page:
# https://ssd.eff.org/tr/blog/how-roll-strong-password-20-sided-dice-and-fandom-inspired-wordlists

import sys
import os
import random

# define phrase file
# phrase file can be selected at the cli
# ./generate_passphrase.py potter

if len(sys.argv) > 1:
    phrases = str(sys.argv[1]) + ".txt"
else:
    phrases = 'trek.txt'

def roll(n):
    # creates the random 20 sided roll
    result = random.randint(1, n)
    return result

def gen_passphrase(x=3, num=3, die=20):
    # iterate through each roll
    i = 1
    passphrase = ""
    while i <= x:
        cur = str(roll(die))
        cur = cur + "-"
        cur = cur + str(roll(die))
        cur = cur + "-"
        cur = cur + str(roll(die))
        # print(cur)
        passphrase = passphrase + lookup(cur)
        i = i + 1
    print("You're passphrase is: ", passphrase)

def lookup(str1):
    # lookup the rolled value (str1)
    results = []
    phrase = ""
    if os.path.isfile(phrases):
        # this is looking for the file in the same directory
        searchfile = open(phrases, "r", encoding="utf8", errors='ignore')
        for line in searchfile:
            if str1 in line:
                out = line.split()
                results = results + out
                phrase = str(results[1]) + " "
        searchfile.close()
        return phrase
    else:
        print('no passphrase file found. exiting.')
        sys.exit()

gen_passphrase()