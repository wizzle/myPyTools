import random
import argparse


def get_char_for_password(what):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return {
        '1': random.choice(alphabet),
        '2': random.choice(alphabet.upper()),
        '3': str(random.randrange(10)),
    }.get(what, '0')


def get_pass(length):
    pw_len = int(length)
    pw = []
    for i in range(pw_len):
        char_type = str(random.randint(1, 3))
        pw.append(get_char_for_password(char_type))
    random.shuffle(pw)
    pwstring = ''.join(pw)
    return pwstring


def get_passwords(count=10, length=10):
    cnt = int(count)
    pwlist = []
    while cnt:
        pwlist.append(get_pass(length))
        cnt -= 1
    return pwlist


parser = argparse.ArgumentParser(description='Password generator.')
parser.add_argument('count_passwords', type=int, help='Count of passwords will be generated.', default=10, nargs='?')
parser.add_argument('length_one_password', type=int, help='Length of one password.', default=12, nargs='?')
args = parser.parse_args()
cp = args.count_passwords
lop = args.length_one_password
passwords = get_passwords(cp, lop)
print(passwords)
