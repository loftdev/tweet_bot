from input_handler import one_letter_input
import unittest


# test  one_letter_input()
def text_input(x):
    return one_letter_input(x)


class TestOneLetterInput(unittest.TestCase):

    def test_input_t(self):
        self.assertEqual(text_input('t'), 't')

    def test_input_l(self):
        self.assertEqual(text_input('l'), 'l')

    def test_input_s(self):
        self.assertEqual(text_input('s'), 's')

    def test_input_exceed(self):
        input_text = [
            "dshojhoh@o@owjwjjjdfjnwrj",
        ]
        result = ""
        for i in input_text:
            result = one_letter_input(i)
            print(result)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
