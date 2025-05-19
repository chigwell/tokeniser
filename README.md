[![PyPI version](https://badge.fury.io/py/tokeniser.svg)](https://badge.fury.io/py/tokeniser)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/tokeniser)](https://pepy.tech/project/tokeniser)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# Tokeniser

`Tokeniser` is a lightweight Python package designed for simple and efficient token counting in text. It uses regular expressions to identify tokens, providing a straightforward approach to tokenization without relying on complex NLP models.

## Installation

To install `Tokeniser`, you can use pip:

```bash
pip install tokeniser
```

## Usage

`Tokeniser` is easy to use in your Python scripts. Here's a basic example:

```python
import tokeniser

text = "Hello, World!"
token_count = tokeniser.estimate_tokens(text)
print(f"Number of tokens: {token_count}")
```

This package is ideal for scenarios where a simple token count is needed, without the overhead of more complex NLP tools.

## Features

- Simple and efficient token counting using regular expressions.
- Lightweight with no dependencies on large NLP models or frameworks.
- Versatile for use in various text processing tasks.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/tokeniser/issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
