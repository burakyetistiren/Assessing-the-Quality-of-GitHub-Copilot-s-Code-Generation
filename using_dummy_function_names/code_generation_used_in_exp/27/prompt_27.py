

def foo(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> foo('Hello')
    'hELLO'
    """
    return string.swapcase()
