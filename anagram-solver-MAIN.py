#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


def main():
    f = open('wordlist.txt', 'r')
    wordlist = f.readlines()
    final = []
    for i in wordlist:
        stripped = i.strip()
        final.append(stripped)
        final.sort(key=len)
    f.close()

#########################################
# INPUT YOUR ANAGRAMS HERE ...

    anagramList = [
        'rsttreak',
        'knetir',
        'gejera',
        'rtoonlc',
        'etscltar',
        'ibomez',
        'e17c0n1c',
        'oruojnb',
        'achriyt',
        'yifgefr',
        ]

#########################################

    word1 = ''
    for j in anagramList:
        for k in final:
            if checkLength(j) == checkLength(k):
                word = list(k)
                if tori(j, word):
                    print k


def checkLength(j):
    length = len(j)
    return length


def tori(j, word):
    for z in j:
        if z not in word:
            return False
        else:
            word.remove(z)
    return True


main()

			
