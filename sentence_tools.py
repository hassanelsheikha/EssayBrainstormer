PUNCTUATION = ['.', '!', '?']

def extract_first_sentence(text: str) -> str:
    """Return the first sentence in <text>. A sentence is defined as a string of
    words that ends with a period. If there is a sentence that occurs after
    another, there must be a space preceeding the second sentence.

    Precondition: <text> contains a sentence.

    >>> extract_first_sentence('Hello there. Nice to meet you.')
    'Hello there.'
    >>> extract_first_sentence('Hello. ')
    'Hello.'
    """
    i = 0
    first_sentence = ''
    while i != len(text):
        try:
            first_sentence += text[i]
            if text[i] in PUNCTUATION and (text[i + 1] == ' ' or
                                           text[i + 1] == '\n'):
                return first_sentence
        except IndexError:
            return first_sentence
        i += 1
    return first_sentence
