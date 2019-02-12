from .check_sentence import check_word_in_sentence
import json

# version of the package
__version__ = '1.1.2'


def awlify(sentence):
    return json.dumps(check_word_in_sentence(sentence))
