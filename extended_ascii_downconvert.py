#!/usr/bin/python3
import sys

# To add characters, use the format `<dec_num>: "<character to replace with>",`
# http://ascii-code.com/ can be used to lookup what a character is.

REPLACEMENTS = {
    145: '\'',# Left Single Quote
    146: '\'',# Right Single Quote
    147: '"', # Left Double Quote
    148: '"', # Right Double Quote
    150: '-', # En Dash
    151: '-', # Em Dash
    160: ' ', # Non-Breaking Space
}

def downconvert_character(char):
    if ord(char) < 128: # Non-Breaking Space
        return char
    elif ord(char) in REPLACEMENTS:
        return REPLACEMENTS[ord(char)]
    else:
        raise KeyError("Unknown Extended ASCII Character")

for file_name in sys.argv[1:]:
    try:
        with open(file_name, 'r', encoding="iso-8859-1") as r:
            contents = r.read()
            with open(file_name, 'w', encoding="ascii") as w:
                for char in contents:
                    w.write(downconvert_character(char))
    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))