#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import argparse


def get_char_for_password(what):
    """
    To avoid ambiguous symbols alphabet is not full.
    Full version of alphabet - 'abcdefghijklmnopqrstuvwxyz'.

    :param: int(what)
    :return: string(char)

    >>> (get_char_for_password(1)).islower()
    True
    >>> (get_char_for_password(2)).isupper()
    True
    >>> (get_char_for_password(3)).isdigit()
    True
    """
    alphabet = 'abcdefghjkmnpqrstuvwxyz'
    return {
        1: random.choice(alphabet),
        2: random.choice(alphabet.upper()),
        3: str(random.randrange(1, 9, 1)),
    }.get(what, 0)


def get_pass(length):
    """
    Function for generate required password.

    :param length:
    :return: string. len(string) == :param length

    >>> len(get_pass(10)) == 10
    True
    >>> (get_pass(10)).isalnum()
    True
    """
    pw_len = int(length)
    pw = ''
    for i in range(pw_len):
        char_type = random.randint(1, 3)
        pw += get_char_for_password(char_type)
    return pw


parser = argparse.ArgumentParser(description='Password generator.')
parser.add_argument('passwords_count', type=int, default=10, help='The number of passwords to be generated. Default 10')
parser.add_argument('password_length', type=int, default=12, help='The length of the password. Default 12')
args = parser.parse_args()
cp = args.passwords_count
if cp > 100:
    cp = 100
pl = args.password_length
passwords = {i + 1: get_pass(pl) for i in range(cp)}
for pass_number in passwords.keys():
    print('%d:\t%s' % (pass_number, passwords[pass_number]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
