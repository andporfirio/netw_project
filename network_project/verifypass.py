#!/ust/bin/python
from __future__ import absolute_import, division, print_function
from getpass import getpass

def getinput(prompt=''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

def get_credentials():
    '''Prompts for and returns, a username and password.'''
    username = getinput("Enter Username: ")
    password = None
    while not password:
        password = getpass("Enter Password: ")
        password_verify = getpass("Retype your Password: ")
        if password != password_verify:
            print("Passwords do not match. Try again.")
            password = None
    return username, password

username, password = get_credentials()
