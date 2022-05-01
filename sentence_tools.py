import nltk
from PyDictionary import PyDictionary
import itertools
from nltk.corpus import wordnet as wn
from GoogleNews import GoogleNews


def get_key_points_google(topic):
    """

    :param topic:
    :return: lst
    
    >>> get_key_points_google('King Kong')
    """
    gn = GoogleNews('en', 'd')
    gn.search(topic)
    gn.getpage(1)
    gn.result()
    return(gn.gettext())

nltk.download('omw-1.4')
PUNCTUATION = ['.', '!', '?']
DICTIONARY = PyDictionary()
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


def get_search_words(s: str) -> dict[str, int]:
    """Returns all possible combinations of words in a string
    """
    out = {}
    lst = s.split()
    for i in range(1, len(lst) + 1):
        for subset in itertools.combinations(lst, i):
            if len(set(subset)) == len(subset):
                out.setdefault(subset, i)
    return out


def main_get_keywords(dic: dict[str, int]) -> list[tuple]:
    """ Fix the list obtained from get_search_words().
    The idea is to get rid of useless searches
    Bad combinations: Adjective, Tense, Preposition, Article, Empty, Noun + (Tense or Preposition)
    >>> main_get_keywords(get_search_words("Usain Bolt is the fastest man"))
    """
    out = []
    for sub_lst in dic:
        if len(sub_lst) >= 3:
            set_of = "0"
            for w in range(len(sub_lst)):
                for tmp in wn.synsets(sub_lst[w]):
                    if tmp.name().split('.')[0] == sub_lst[w]:
                        set_of += tmp.pos()
            d = {}
            for i in set_of:
                d.setdefault(i, 0)
                d[i] += 1
            most_common = max(d, key=d.get)
            set_of = most_common

            if set_of == 'n':
                out.append(sub_lst)
    return out


def keywords(phrase: str) -> list[str]:
    """ Given a <phrase>, return relatively-sensible combinations of the words
    that comprise it.
    >>> keywords('Usain bolt is the fastest man.')
    """
    ans = [phrase]
    unformatted = main_get_keywords(get_search_words(phrase))
    for keyword in unformatted:
        ans.append(' '.join(keyword))
    if phrase not in ans:
        ans.insert(0, phrase)
    try:
        temp = ans[1:]
        temp.remove(phrase)
        ans[1:] = temp
        return ans
    except ValueError:
        return ans


if __name__ == '__main__':
    import doctest

    doctest.testmod()
