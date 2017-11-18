#!/usr/bin/python

import os
import re

from base64 import b64encode

def get_randr_str():
    s = os.urandom(128)

    return b64encode(s)


def main():
    match = list()

    while len(match) == 0:
        match = re.findall('[0-9]', get_randr_str())

        if match:
            num = int(''.join(match))
            print num % 90

            break

main()
