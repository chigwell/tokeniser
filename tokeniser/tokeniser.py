import re

def estimate_tokens(text):
    tokens = re.findall(r"[\w']+|[.,!?;]", text)
    return len(tokens)
