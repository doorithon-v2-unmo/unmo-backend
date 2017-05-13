from random import randint

LETTERS_SET = "0123456789abcdefghijklmnopqrstuvwxyz"


def build_randomstring(length):
    randomstring = ""
    for _ in range(length):
        randomstring += LETTERS_SET[randint(0, len(LETTERS_SET) - 1)]
    return randomstring
