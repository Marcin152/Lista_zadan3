import random
import base64
import logging

#Zadanie 3
def generator_hasla():
    ints = range(33,127)
    password = ''

    for i in range(0, 16):
        password += chr(random.choice(ints))

    if i >= 15:
        return password

#Zadanie 2
def encode_base64():
    encoded = base64.b64encode(b'klawiatura')
    return encoded

#Zadanie 1
def logging_function():
    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
    logging.warning('This is a Warning')
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
