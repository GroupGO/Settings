#!/usr/bin/env python


"""
Author: Henry Ehlers
WUR_Number: 921013218060

A collection of function responsible for loading the settings that govern the settings the
pipeline.

In order to provide readable and understandable code, the right indentation margin has been
increased from 79 to 99 characters, which remains in line with Python-Style-Recommendation (
https://www.python.org/dev/peps/pep-0008/) .This allows for longer, more descriptive variable
and function names, as well as more extensive doc-strings.
"""


import os


def import_input(input_file_path):
    """
    Function to load the contents of an input text_file and return it as a dictionary.

    :param input_file_path:
    :return:
    """
    text_file_assertion(input_file_path)
    settings = {}
    with open(input_file_path, 'r') as input_file:
        for header, settings in load_record(input_file):
            settings[header] = settings
    return settings


def text_file_assertion(file_path):
    """
    Method to assert the type of the input file name, the file's presence and type.

    :param file_path: The file name as a string to be be tested.
    """
    assert isinstance(file_path, str), 'Given file path must be of type string.'
    assert os.path.exists(file_path), 'Given file path does not exist'
    assert file_path.split('.')[-1] == 'txt', 'Given file extension is not ".txt".'


def load_record(input_file):
    """
    Function to yield the contents of the input file one at a time.

    :param input_file: The opened file whose contents are to be loaded.
    :return: Yield the contents of the file (header and settings) one record at a time.
    """
    header, settings = '', []
    for line in input_file:
        line = line.strip()
        if line[0] == '#':
            continue
        if line[0] == '@':
            if header:
                yield header, settings
            header = line[1:]
        elif header:
            record_settings = (line.split(','))
            settings.append([record_settings[1], record_settings[2]])
    yield header, settings


import_input('Test_Input.txt')
