"""
A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each
other if the first string's letters can be rearranged to form the second string. In other words, both strings must
contain the same exact letters in the same exact frequency. For example, 'bacdc' and 'dcbac' are anagrams,
but 'bacdc' and 'dcbad' are not.

The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum
number of character deletions required to make the two strings anagrams. Determine this number.

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character
deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

Example
a = 'cde'
b = 'dcf'
Delete e from a and f from b so that the remaining strings are cd and dc which are anagrams.
This takes 2 character deletions.
"""
import pytest


def count_deletions_for_anagram(a, b):
    # Write your code here
    hash_a = {}
    hash_b = {}
    deletions = 0
    for i in a:
        if i not in hash_a:
            hash_a[i] = 1
        else:
            hash_a[i] += 1
    for i in b:
        if i not in hash_b:
            hash_b[i] = 1
        else:
            hash_b[i] += 1

    all_chars = set(a) | set(b)

    for char in all_chars:
        deletions += abs(hash_a.get(char, 0) - hash_b.get(char, 0))

    return deletions

@pytest.mark.parametrize(
    "a, b, deletions", [
        #("cde", "abc", 4),
        ("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke", 30),
        #("showman", "woman", 2)
    ]
)
def test_count_deletions_for_anagram(a, b, deletions):
    assert count_deletions_for_anagram(a, b) == deletions

def alternating_characters(s):
    new_s = ''
    deletions = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            deletions += 1
        else:
            new_s += s[i]

    print(f"\n{new_s}")
    return deletions


@pytest.mark.parametrize(
    "s, deletions", [
        ("AAAA", 3),
        ("BBBBB", 4),
        ("ABABABAB", 0),
        ("BABABA", 0),
        ("AAABBB", 4),
        ("AAABBBAABB", 6),
        ("AABBAABB", 4),
        ("ABABABAA", 1),
        ("ABBABBAA", 3),
        ("ABABAAABABBABABBBBABBBABBBA", 10),
        ("ABABAAABABBABABBBBABBBABBBAABABAAABABBABABBBBABBBABBBA", 21),
        ("ABABAAABABBABABBBBABBBABBBAABABAAABABBABABBBBABBBABBBAABABAAABABBABABBBBABBBABBBA", 32)
    ]
)
def test_alternating_characters(s, deletions):
    assert alternating_characters(s) == deletions