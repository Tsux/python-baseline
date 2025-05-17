import math
import pytest
'''
There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

Example
'''
s = 'abcac'
n = 10
'''
The substring we consider is 'abcacabcac', the first 10 characters of the infinite string. 
There are 4 occurrences of a in the substring.
'''

def repeated_string(s, n):
    if "a" not in s or n == 0:
        return 0

    rep, rem = 1, 0
    if len(s) < n:
        # TODO: Find the manual way to round up a number, should be something close to:
        # if n/len(s) % 1 != 0 else int(n/len(s))
        rep, rem = math.ceil(n / len(s)), n % len(s)
    elif len(s) > n:
        s = s[:n]

    count = 0
    for i in s:
        count += 1 if i == "a" else 0

    if rem == 0:
        return rep * count
    else:
        altc = 0
        for i in s[:rem]:
            altc += 1 if i == "a" else 0

        return (rep - 1) * count + altc

@pytest.mark.parametrize(
    "string,n,expected", [
        ('abcac',10, 4),
        ('aba', 10, 7),
        ('asklasasaasasdsasdasmloi', 10, 5),
        ('a', 1000000000000, 1000000000000),
        (
                'aaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                110,
                106,
         ),
        (
                'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                534802106762,
                534802106762
         )
    ]
)
def test_repeated_string(string, n, expected):
    assert repeated_string(string, n) == expected
