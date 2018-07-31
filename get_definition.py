import json
from difflib import SequenceMatcher, get_close_matches


"""
    This program loads a json file of words and their meanings into a python dictionary and 
    allows a user tp find the meaning of a word. It also auto suggests similar words if the word entered 
    is not found.
"""
word = input("type a word to get its meaning:")
word_dict = json.load(open('data.json'))


def get_meaning(word):
    """
    :param wrd:
    :return: definition of wrd
    """

    word = word.lower()

    """
        check for lowercase, upper case and title case
    """
    if word in word_dict:
        return ''.join(word_dict[word])
    elif word.title() in word_dict:
        return ''.join(word_dict[word.title()])
    elif word.upper() in word_dict:
        return ''.join(word_dict[word.upper()])
    else:
        # find a word that closely matches the entered word
        close_matches = get_close_matches(word, word_dict.keys(), cutoff=0.8)
        if len(close_matches) == 0:
            return "Word not found"

        yes_no = input("Did you mean {}{} (y)es or (n)o: ".format(str(close_matches[0]), "?"))
        if yes_no == 'y':
            return ''.join(word_dict[close_matches[0]])
        else:
            return "Ok Bye..."


print(get_meaning(word))
