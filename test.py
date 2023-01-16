import random
import sys
import time


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)


time.sleep(2)
print_slow("viktor är en horunge")
