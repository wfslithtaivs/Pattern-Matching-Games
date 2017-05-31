"""Check if pattern matches.

Given a "pattern string" starting with "a" and including only "a" and "b"
characters, check to see if a provided string matches that pattern.

For example, the pattern "aaba" matches the string "foofoogofoo" but not
"foofoofoodog".

Patterns can only contain a and b and must start with a:

    >>> pattern_match("b", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("A", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("abc", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

The pattern can contain only a's:

    >>> pattern_match("a", "foo")
    True

    >>> pattern_match("aa", "foofoo")
    True

    >>> pattern_match("aa", "foobar")
    False

It's possible for a to be zero-length (a='', b='hi'):

    >>> pattern_match("abbab", "hihihi")
    True

Or b to be zero-length (a='foo', b=''):

    >>> pattern_match("aaba", "foofoofoo")
    True

Or even for a and b both to be zero-length (a='', b=''):

    >>> pattern_match("abab", "")
    True

But, more typically, both are non-zero length:

    >>> pattern_match("aa", "foodog")
    False

    >>> pattern_match("aaba" ,"foofoobarfoo")
    True

    >>> pattern_match("ababab", "foobarfoobarfoobar")
    True

Tricky: (a='foo', b='foobar'):

    >>> pattern_match("aba" ,"foofoobarfoo")
    True

Now non-toy tests:

    >>> pattern_match("abba" ,"foobarbarfod")
    False
"""

def is_solution(solution, pattern, astring):
    """Check if the solution match string"""

    stg = {'a' : astring[ :solution[0]] }

    if solution[1] == 0:
        stg['b'] = ""
    else:
        first_pos_b = solution[0] * pattern.index("b")
        stg['b'] = astring[first_pos_b : first_pos_b + solution[1]]

    res = [stg[item] for item in pattern]

    return "".join(res) == astring


def pattern_match(pattern, astring):
    """Can we make this pattern match this string?"""

    # Q&D sanity check on pattern

    assert (pattern.replace("a", "").replace("b", "") == ""
            and pattern.startswith("a")), "invalid pattern"

    str_len = len(astring)
    n = tuple(pattern.count(x) for x in ('a', 'b'))

    if any(el == 1 for el in n) : 
        return True

    for i in range(str_len/n[0] + 1) :
        if n[1] != 0:
            x = (i, (str_len - i*n[0]) / n[1])
        else:
            x = (i, 0)

        assert (x[1] >= 0), "Unrealistic len" 
        assert n[1] == 0 or (x[0] * n[0] + x[1] * n[1] == str_len), \
            "Out of len: " + str(x)

        if is_solution(x, pattern, astring):
            return True

    return False


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WE'RE WELL-MATCHED!\n"
