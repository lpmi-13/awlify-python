import json
import unittest
import subprocess


def pipe_through_stdout(command):
    return subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            shell=True)


def convert_to_bytes_with_encoding(data):
    return bytes('{}\n'.format(json.dumps(data)),
                 encoding='utf-8')


class TestCheckSentence(unittest.TestCase):

    def test_pass_no_command_line_arguments(self):
        command = "python3 -m awlify"
        expected = b'please enter a sentence to search\n'
        output = pipe_through_stdout(command)
        (result, err) = output.communicate()
        self.assertEqual(result, expected)

    """
    bash is treating all command line args as strings, so
    this test only works on linux machines
    """
    def test_pass_non_string_command_line_arguments(self):
        command = "python3 -m awlify 12345"
        json_string = {
                     "data": {
                       "sentence": "12345",
                       "awl_words": []
                     }
                   }
        expected = convert_to_bytes_with_encoding(json_string)
        output = pipe_through_stdout(command)
        (result, err) = output.communicate()
        self.assertEqual(result, expected)

    def test_single_command_line_argument(self):
        command = "python3 -m awlify 'pass this test'"
        json_string = {
                     "data": {
                       "sentence": "pass this test",
                       "awl_words": []
                     }
                   }
        expected = convert_to_bytes_with_encoding(json_string)
        output = pipe_through_stdout(command)
        (result, err) = output.communicate()
        self.assertEqual(result, expected)

    def test_more_than_one_command_line_argument(self):
        command = "python3 -m awlify 'only return this' 'do not return this'"
        json_string = {
                     "data": {
                       "sentence": "only return this",
                       "awl_words": []
                     }
                   }
        expected = convert_to_bytes_with_encoding(json_string)
        output = pipe_through_stdout(command)
        (result, err) = output.communicate()
        self.assertEqual(result, expected)
