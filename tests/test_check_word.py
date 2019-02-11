import unittest
from awlify.utils.check_word import check_word_in_list


class CheckWordTest(unittest.TestCase):

    def test_word_not_in_awl(self):
        word = 'simple'
        result = check_word_in_list(word)
        self.assertEqual(result, None)

    def test_head_word_in_awl(self):
        word = 'economy'
        expected = {'head': 'economy', 'sublist': 1}
        result = check_word_in_list(word)
        self.assertEqual(expected, result)

    def test_sublist_word_in_awl(self):
        word = 'economical'
        expected = {'head': 'economy', 'sublist': 1}
        result = check_word_in_list(word)
        self.assertEqual(expected, result)

    def test_empty_input(self):
        word = ''
        result = check_word_in_list(word)
        self.assertEqual(result, None)

    def test_numeric_input(self):
        word = 1234
        result = check_word_in_list(word)
        self.assertEqual(result, None)

    def test_list_input(self):
        word = ['this', 'is', 'not', 'a', 'string']
        result = check_word_in_list(word)
        self.assertEqual(result, None)
