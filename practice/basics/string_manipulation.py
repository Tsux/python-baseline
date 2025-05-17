# Return first repeated element in string
import pytest

def get_most_repeated(s: str):
    """
    Returns most repeated char in string
    :param s:
    :return:
    """
    rep_hashmap = {}
    max = 1
    max_c = ''
    is_repeated_max = False
    s = s.lower().replace(' ', '')
    for i in s:
        if i not in rep_hashmap.keys():
            rep_hashmap[i] = 1
        else:
            val = rep_hashmap.get(i) + 1
            rep_hashmap[i] = val
            is_repeated_max = val == max
            max, max_c = [val, i] if val > max else [max, max_c]


    if max == 1 or is_repeated_max:
        return None

    return max_c

def get_first_repeated(s: str):
    """
    Returns first repeated char in string
    :param s:
    :return: the first repeated char in string, None if no duplicated found
    """
    rep_hash = []
    s = s.lower().replace(' ', '')
    for i in s:
        if i not in rep_hash:
            rep_hash.append(i)
        else:
            return i

    return None

@pytest.mark.parametrize(
    "sample,expected", [
        ('Tsunekichi', 'i'),
        ('Boomerang', 'o'),
        ('Yay', 'y'),
        ('eeeew', 'e'),
        ('No rep', None)
    ]
)
def test_get_first_repeated(sample, expected):
    assert get_first_repeated(sample) == expected

@pytest.mark.parametrize(
    "sample,expected", [
        ('Tsunekichi', 'i'),
        ('Tsunekichi Maldonado Matias', 'a'),
        ('Anita Pitt', 't'),
        ('Rooger Labbito', 'o'),
        ('Anita', 'a'),
        ('Boomerang', 'o'),
        ('Yay', 'y'),
        ('eeeew', 'e'),
        ('No rep', None),
        ('Tsunekichi Maldonado', None),
        ('Anita Split', None),
        ('Rooger Rabbito', None),
    ]
)
def test_get_most_repeated(sample, expected):
    assert get_most_repeated(sample) == expected

