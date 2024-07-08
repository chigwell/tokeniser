'''
The `tokeniser` package is a lightweight Python library designed for simple and efficient token counting in text.

This file, 'tokeniser.py', contains the main implementation of this functionality.
It uses regular expressions to estimate tokens in the given text.
'''
    }

import re

def estimate_tokens(text):
    tokens = re.findall(r"[\w']+|[.,!?;]", text)
    return len(tokens)
