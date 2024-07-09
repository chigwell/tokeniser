'''
This is a Python script for 'Tokeniser', which is a package for simple token counting in text.
The main functionality is provided by the 'estimate_tokens' function imported from the '.tokeniser' module.
This file does not contain any direct code execution but rather imports and exports functionalities.
'''


import re

def estimate_tokens(text):
    tokens = re.findall(r"[\w']+|[.,!?;]", text)
    return len(tokens)
