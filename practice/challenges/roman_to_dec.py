"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.
"""
import pytest


def roman_to_int(s: str) -> int:
    d_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
    decimal = 0
    for i in range(len(s)):
        # Look ahead to the next character if it exists
        if i + 1 < len(s) and d_map[s[i]] < d_map[s[i + 1]]:
            decimal -= d_map[s[i]]  # Subtractive case
        else:
            decimal += d_map[s[i]]  # Additive case
    return decimal

@pytest.mark.parametrize(
    "roman,integer", [
        ("I", 1),
        ("III", 3),
        ("XXVII", 27),
        ("LXXXIX", 89),
        ("MCMXCIV", 1994),
        ("MMMCMXCIX", 3999),
        ("MMMMMMM", 7000)
    ]
)
def test_roman_to_int(roman, integer):
    assert roman_to_int(roman) == integer