import unittest
from awlify.check_sentence import check_word_in_sentence


class TestCheckSentence(unittest.TestCase):

    def test_sentence_with_awl_word(self):
        sentence = 'this is an economical sentence'
        expected = {
          'data': {
            'sentence': 'this is an economical sentence',
            'awl_words': [
              {
                'index': 3,
                'word': 'economical',
                'meta': {
                  'head': 'economy',
                  'sublist': 1
                }
              }
            ]
          }
        }
        result = check_word_in_sentence(sentence)
        self.assertEqual(result, expected)

    def test_sentence_without_awl_word(self):
        sentence = 'this has no fun words'
        expected = {
          'data': {
            'sentence': 'this has no fun words',
            'awl_words': []
          }
        }
        result = check_word_in_sentence(sentence)
        self.assertEqual(result, expected)

    def test_sentence_with_two_awl_words(self):
        sentence = 'we spent all our time analyzing the evidence'
        expected = {
          'data': {
            'sentence': 'we spent all our time analyzing the '
                        'evidence',
            'awl_words': [
              {
                'index': 5,
                'word': 'analyzing',
                'meta': {
                  'head': 'analyse',
                  'sublist': 1
                }
              },
              {
                'index': 7,
                'word': 'evidence',
                'meta': {
                  'head': 'evident',
                  'sublist': 1
                }
              }
            ]
          }
        }
        result = check_word_in_sentence(sentence)
        self.assertEqual(result, expected)

    def test_sentence_with_blank_string(self):
        sentence = ''
        expected = {
          'data': {
            'sentence': '',
            'awl_words': []
          }
        }
        result = check_word_in_sentence(sentence)
        self.assertEqual(result, expected)

    def test_sentence_with_numeric_input(self):
        sentence = 123456
        with self.assertRaises(Exception):
            check_word_in_sentence(sentence)

    def test_sentence_with_list_input(self):
        sentence = ['this', 'is', 'not', 'a', 'string']
        with self.assertRaises(Exception):
            check_word_in_sentence(sentence)
