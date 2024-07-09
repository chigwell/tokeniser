"""
This Python module is part of a lightweight token counting package called `Tokeniser`. It contains the main functionality for estimating tokens in text using regular expressions. The code defines functions such as `estimate_tokens` that take input strings and return the count of tokens identified by the function. This module can be easily imported and used for simple token counting tasks without relying on complex NLP models.
"""

import re


def estimate_tokens(text):
    tokens = re.findall(r"[\w']+|[.,!?;]", text)
    return len(tokens)
