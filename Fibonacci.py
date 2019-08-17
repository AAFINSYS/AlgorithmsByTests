import unittest


def recursive_fibonacci(input_number):
    if input_number in (0, 1):
        return input_number

    return recursive_fibonacci(input_number-1) + recursive_fibonacci(input_number-2)


class TestRecursiveFibonacci(unittest.TestCase):
    def test_should_return_zero_when_input_is_zero(self):
        actual = recursive_fibonacci(0)

        self.assertEqual(actual, 0)

    def test_should_return_one_when_input_number_is_one(self):
        actual = recursive_fibonacci(1)

        self.assertEqual(actual, 1)

    def test_should_return_one_when_input_number_is_two(self):
        actual = recursive_fibonacci(2)

        self.assertEqual(actual, 1)

    def test_should_return_610_when_input_number_is_15(self):
        actual = recursive_fibonacci(15)

        self.assertEqual(actual, 610)

    def test_should_return_same_result_for_15_when_processing_sum_from_the_results_from_13_and_14(self):
        self.assertEqual(recursive_fibonacci(15), recursive_fibonacci(14) + recursive_fibonacci(13))


def tail_recursive_fibonacci(input_number, a = 0, b = 1):
    if input_number == 0:
        return a
    if input_number == 1:
        return b

    return tail_recursive_fibonacci(input_number-1, b, a+b)


class TestTailRecursiveFibonacci(unittest.TestCase):
    def test_should_return_zero_when_input_is_zero(self):
        actual = tail_recursive_fibonacci(0)

        self.assertEqual(actual, 0)

    def test_should_return_one_when_input_number_is_one(self):
        actual = tail_recursive_fibonacci(1)

        self.assertEqual(actual, 1)

    def test_should_return_one_when_input_number_is_two(self):
        actual = tail_recursive_fibonacci(2)

        self.assertEqual(actual, 1)

    def test_should_return_610_when_input_number_is_15(self):
        actual = tail_recursive_fibonacci(15)

        self.assertEqual(actual, 610)

    def test_should_return_same_result_for_15_when_processing_sum_from_the_results_from_13_and_14(self):
        self.assertEqual(tail_recursive_fibonacci(15), tail_recursive_fibonacci(14) + tail_recursive_fibonacci(13))


def iterative_fibonacci(input_number):
    if input_number in (0, 1):
        return input_number

    value_fibo_n_minus_one = 1
    value_fibo_n_minus_two = 0

    for i in range(2, input_number+1):
        value_fibo_n_minus_two, value_fibo_n_minus_one = value_fibo_n_minus_one, value_fibo_n_minus_one + value_fibo_n_minus_two

    return value_fibo_n_minus_one


class TestIterativeFibonacci(unittest.TestCase):
    def test_should_return_zero_when_input_is_zero(self):
        actual = iterative_fibonacci(0)

        self.assertEqual(actual, 0)

    def test_should_return_one_when_input_number_is_one(self):
        actual = iterative_fibonacci(1)

        self.assertEqual(actual, 1)

    def test_should_return_one_when_input_number_is_two(self):
        actual = iterative_fibonacci(2)

        self.assertEqual(actual, 1)

    def test_should_return_610_when_input_number_is_15(self):
        actual = iterative_fibonacci(15)

        self.assertEqual(actual, 610)

    def test_should_return_same_result_for_15_when_processing_sum_from_the_results_from_13_and_14(self):
        self.assertEqual(iterative_fibonacci(15), iterative_fibonacci(14) + iterative_fibonacci(13))


if __name__ == "__main__":
    unittest.main()