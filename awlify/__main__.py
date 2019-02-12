from .check_sentence import check_word_in_sentence
import json
import sys

# version of the package
__version__ = '1.1.2'


def return_json_data(sentence):
    return json.dumps(check_word_in_sentence(sentence))


def main():

    if len(sys.argv) > 1:
        print(return_json_data(sys.argv[1]))

    else:
        print('please enter a sentence to search')


if __name__ == '__main__':
    main()
