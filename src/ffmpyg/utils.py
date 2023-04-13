''' Contains helper methods that aren't related directly to FFMPEG
'''
import random
import string
from typing import List, Set


DOUBLE_QUOTE = '"'


def ensureQuoted(s: str) -> str:
    ''' Ensures a string containing spaces is fully enclosed
    between double quotes
    '''
    if ' ' not in s:
        return s
    res = s
    if s.startswith(DOUBLE_QUOTE):
        res = DOUBLE_QUOTE + res
    if s.endswith(DOUBLE_QUOTE):
        res = res + DOUBLE_QUOTE
    return res


def assertTrue(condition: bool, message: str, *arguments) -> None:
    ''' Like assert, but without its optimization issues
    '''
    if not condition:
        raise AssertionError(message.format(*arguments))


def flatten_dict_join(d: dict) -> dict:
    ''' Returns a dictionnary with similar content but no nested dictionnary value
    WARNING: requires all keys to be str !
    Strategy to conserve key uniqueness is `key joining`:  d[k1][k2] -> d[k1.k2]
    '''
    dflat = {}
    for k, v in d.items():
        assertTrue(isinstance(k, str), "Key {} is a {}, not str !", k, type(k))
        if isinstance(v, dict):
            d2 = flatten_dict_join(v)
            for k2, v2 in d2.items():
                assertTrue(isinstance(k2, str), "Key {} is a {}, not str !", k2, type(k2))
                k1_2 = k + '.' + k2
                assertTrue(k1_2 not in dflat, "Collision: key {} already in dict !", k1_2)
                dflat[k1_2] = v2
            continue

        assertTrue(k not in dflat, "Collision: key {} already in dict !", k)
        dflat[k] = v

    return dflat


def dict_difference(dictA: dict, dictB: dict) -> dict:
    ''' Performs dictA - dictB on the key-value pairs: Returns a dictionnary
    with all items from dictA minus the key-value pairs in common with dictB
    '''
    diff = {
        k: dict_difference(v_a, dictB[k]) if isinstance(v_a, dict) and k in dictB else v_a
        for k, v_a in dictA.items()
        if (k not in dictB) or (isinstance(v_a, dict) or v_a != dictB[k])
    }
    for k in list(diff.keys()):
        if diff[k] == {}:
            del diff[k]
    return diff


def random_words(n: int, length: int, used_words: Set[str]) -> List[str]:
    ''' Generates random word (lowercase) of given length; if `used_words` is provided,
    it will avoid already-generated words
    '''
    res: List[str] = []
    while len(res) < n:
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length)) # nosec B311
        if used_words is not None:
            if word in used_words:
                continue
            used_words.add(word)
        res.append(word)
    return res
