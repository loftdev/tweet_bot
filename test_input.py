from unittest import TestCase
from unittest.mock import patch
from input_handler import one_letter_input


# test  one_letter_input()
def answer():
    ans = one_letter_input('l')
    if ans == 't':
        return 'you entered t'
    if ans == 'l':
        return 'you entered l'
    if ans == 's':
        return 'you entered s'


class Test(TestCase):

    # get_input will return 'yes' during this test
    @patch('yourmodule.get_input', return_value='t')
    def test_answer_t(self, input):
        self.assertEqual(answer(), 'you entered t')

    @patch('yourmodule.get_input', return_value='l')
    def test_answer_l(self, input):
        self.assertEqual(answer(), 'you entered l')

    @patch('yourmodule.get_input', return_value='s')
    def test_answer_s(self, input):
        self.assertEqual(answer(), 'you entered s')