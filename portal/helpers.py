import email
import os
import random
import re
import string

# def get_random_characters(string_length=3):
#     return ''.join(random.choice(string.ascii_letters) for x in range(string_length))


def get_random_numbers(string_length=3):
    return ''.join(random.choice(string.digits) for x in range(string_length))

def validate_gmail(gmail):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, gmail)):
        return True
    return False