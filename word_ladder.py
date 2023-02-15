#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    with open(dictionary_file, 'r') as f:
        text = f.read()
    dictionary = text.split()
    print(dictionary)
    x = []
    x.append(start_word)
    y = deque()
    y.append(x)
    if start_word == end_word:
        return x
    while len(y) != 0:
        newy = y.popleft()
        z = copy.copy(dictionary)
        for i in z:
            if _adjacent(i, newy[-1]) is True:
                if i == end_word:
                    newy.append(i)
                    return newy
                else:
                    new = copy.copy(newy)
                    new.append(i)
                    y.append(new)
                    dictionary.remove(i)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder == [] or ladder is None:
        return False
    if len(ladder) == 1:
        return True
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) == len(word2):
        ct = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                ct += 1
        if ct > 1:
            return False
        elif ct == 0:
            return False
        else:
            return True
    else:
        return False
