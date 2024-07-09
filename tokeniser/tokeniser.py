'''
This Python script defines a function to estimate the number of tokens in a text using regular expressions.
The `estimate_tokens` function takes a text string as input and returns an integer representing the estimated number of tokens in that text.
'''


import re

def estimate_tokens(text):
    tokens = re.findall(r"[\w']+|[.,!?;]", text)
    return len(tokens)
