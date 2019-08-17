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


def process_integer_to_string(param):
    return chr(param + ord("0"))


class TestStringAlgorithmConvertingNumbersToStrings(unittest.TestCase):
    def test_should_return_string_one_when_number_one_is_processed(self):
        actual = process_integer_to_string(1)

        self.assertEqual(actual, "1")

    def test_should_return_string_five_when_number_five_is_processed(self):
        actual = process_integer_to_string(5)

        self.assertEqual(actual, "5")

    @unittest.skip("skip")
    def test_should_return_string_fifteen_when_number_fifteen_is_processed(self):
        actual = process_integer_to_string(15)

        self.assertEqual(actual, "15")


def even_first_sort_array(array_to_sort):
    first_even_position_to_inspect = 0
    first_odd_position_to_inspect = len(array_to_sort) - 1

    while first_even_position_to_inspect < first_odd_position_to_inspect:
        if array_to_sort[first_even_position_to_inspect] % 2 == 0:
            first_even_position_to_inspect += 1
        else:
            array_to_sort[first_even_position_to_inspect], array_to_sort[first_odd_position_to_inspect] = \
                array_to_sort[first_odd_position_to_inspect], array_to_sort[first_even_position_to_inspect]

            first_odd_position_to_inspect -= 1


class TestArrayBootcamp(unittest.TestCase):
    def test_should_return_even_first_sorted_array_when_two_element_integer_array_is_processed(self):
        actual = [1, 2]

        even_first_sort_array(actual)

        self.assertListEqual(actual, [2, 1])

    def test_should_return_even_first_sorted_array_when_three_element_integer_array_is_processed(self):
        actual = [1, 2, 3]

        even_first_sort_array(actual)

        self.assertListEqual(actual, [2, 3, 1])

    def test_should_return_even_first_sorted_array_when_eleven_element_integer_array_is_processed(self):
        actual = [1, 2, 0, 7, 9, 11, 5, 6, 8, 3, 12]

        even_first_sort_array(actual)

        self.assertListEqual(actual, [12, 2, 0, 8, 6, 5, 11, 9, 3, 7, 1])


class TestArray_MaxProfitFromBuyOnceSellOnce(unittest.TestCase):
    def should_return_profit_when_price_array_contains_two_prices(self):
        actual = 0

        priceArray = [200, 220]
        actual = 20

        self.assertEqual(actual, 20)


if __name__ == "__main__":
    unittest.main()