"""
services.py: Business logic for generating palindromes and non-palindromes.

This module contains the `generate_string` function, which is responsible for
creating palindrome and non-palindrome strings based on user input.

Author: Daria S
"""

import random
import string
from typing import Optional


def generate_string(palindrome: bool, length: int = 6) -> str:
    """
    Generate a palindrome or non-palindrome string.

    :param palindrome: bool
        A required boolean flag indicating whether to generate a palindrome.
    :param length: int, optional
        The length of the string to generate. Defaults to 6.
        Must be between 1 and 30 inclusive.

    :raises ValueError:
        If `length` is less than 1 or greater than 30.

    :return: str
        The generated string, either a palindrome or a non-palindrome.

    :example:
        >>> generate_string(palindrome=True, length=5)
        'abcba'

        >>> generate_string(palindrome=False, length=5)
        'abcde'
    """
    if not (1 <= length <= 30):
        raise ValueError("Length must be between 1 and 30.")

    if palindrome:
        # Generate a palindrome
        half_length: int = length // 2
        half: str = ''.join(random.choices(string.ascii_lowercase, k=half_length))
        if length % 2 == 0:
            return half + half[::-1]
        else:
            middle: str = random.choice(string.ascii_lowercase)
            return half + middle + half[::-1]
    else:
        # Generate a non-palindrome
        while True:
            result: str = ''.join(random.choices(string.ascii_lowercase, k=length))
            if result != result[::-1]:
                return result
