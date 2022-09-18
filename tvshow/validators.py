from tvshow import api_keys

import re
import requests

""" User validation. """
def validate_username(username):
    return re.match(r'^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$', username)

class EmailCheck():
    @staticmethod
    def email_is_invalid_message():
        return 'The provided email is invalid.'

    @staticmethod
    def email_is_unknown_message():
        return 'The provided email is unknown.'

    def validate_email(self, email):
        e = EmailCheck()
        api_key = api_keys.realemail_api_key
        response = requests.get(
            "https://isitarealemail.com/api/email/validate",
            params={'email': email},
            headers={'Authorization': 'Bearer' + api_key }
        )
        status = response.json()['status']
        if status == 'valid':
            return True
        elif status == 'invalid':
            self.message = e.email_is_invalid_message()
            return False
        else:
            self.message = e.email_is_unknown_message()
            return False

class PasswordCheck():
    @staticmethod
    def password_len_message():
        return 'Make sure your password is at least 8 letters.'

    @staticmethod
    def password_contains_number_message():
        return 'Make sure your password has a number in it.'

    @staticmethod
    def password_contains_capitalletter_message():
        return 'Make sure your password has a capital letter in it.'

    def validate_password(self, password):
        p = PasswordCheck()
        if len(password) < 8:
            self.message = p.password_len_message()
            return False
        elif re.search('[0-9]', password) is None:
            self.message = p.password_contains_number_message()
            return False
        elif re.search('[A-Z]', password) is None:
            self.message = p.password_contains_capitalletter_message()
            return False
        else:
            return True

""" Tvshow validation. """
def validate_tvshow_autor(autor):
    return re.search(r'/^[a-z ,.-]+$/i', autor)

def validate_tvshow_language(language):
    return re.search('[A-Z][a-z]', language)