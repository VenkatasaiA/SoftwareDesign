import re
import random
import string



class Citizen:
    def __init__(self, First_Name, Address_1,Address_2, Zip_Code, City_name):
        self.id = id
        self.name = self._is_valid_name(name)
        self.email = self._is_valid_email(email)
        self.age = self._is_valid_age(age)

    def _is_valid_name(self, name):
        if len(name) > 20:
            raise ValueError("Name cannot exceed 20 characters.")
        return name

    def _is_valid_email(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, email):
            raise ValueError("It's not an email address.")
        return email

    def _is_valid_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        return age

def get_random_characters(string_length=3):
    return ''.join(random.choice(string.ascii_letters) for x in range(string_length))


def get_random_numbers(string_length=3):
    return ''.join(random.choice(string.digits) for x in range(string_length))


def validate_gmail(gmail):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, gmail)):
        return True
    return False