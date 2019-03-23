import unittest
import math


def process_string_to_integer(param):
    return_value = 0
    multiplicator = 1

    if param[0] == "-":
        multiplicator = -1
        param = param[1::]

    for position, char_digit in enumerate(reversed(param)):
        return_value += (ord(char_digit) - ord("0")) * math.pow(10, position)

    return multiplicator * return_value


class TestsStringAlgorithmConvertingNumbersToStrings(unittest.TestCase):
    def test_should_return_number_one_when_a_string_representing_one_is_processed(self):
        actual = process_string_to_integer("1")

        self.assertEqual(actual, 1)

    def test_should_return_number_twelve_when_a_string_representing_twelve_is_processed(self):
        actual = process_string_to_integer("12")

        self.assertEqual(actual, 12)

    def test_should_return_number_minus_fifty_five_when_a_string_representing_minus_fifty_five_is_processed(self):
        actual = process_string_to_integer("-55")

        self.assertEqual(actual, -55)

    def test_should_return_number_minus_1234_when_a_string_representing_minus_1234_is_processed(self):
        actual = process_string_to_integer("-1234")

        self.assertEqual(actual, -1234)


if __name__ == "__main__":
    unittest.main()