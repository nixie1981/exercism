def abbreviate(words):
    """
    Returns the first letters of words in a string.
    
    Parameters
    ----------
    words : string
        An input string
    
    Returns
    -------
    result : string
        A string made up of capitalized first letters
    
    Example
    -------
    >>> abbreviate("My precious _monkey")
    MPM
    
    """
    letters = []
    words = words.replace('_', ' ').replace('-', ' ')
    words_split = words.split()
    letters = [word[0] for word in words_split]
    result = ''.join(letters).upper()
    return result
