from art import *
import re
word = input("Enter a string: ")
regex = "[a-zA-Z]"


def texttoascii(word):
    if (re.match(regex, word) != None):
        asciiword = text2art(word, font="Banner")
        asciiword = asciiword.replace("#", "*")
        print(asciiword)
    else:
        print("Data is not a string.")


texttoascii(word)
