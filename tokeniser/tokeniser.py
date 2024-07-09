'''
This file implements a simple text tokenizer using regular expressions.

The `estimate_tokens` function calculates the number of tokens in a given text by splitting it into words based on whitespace and counting them.
'''
                       }

import re

def estimate_tokens(text):
    tokens = re.findall(r"[\w']+|[.,!?;]", text)
    return len(tokens)
