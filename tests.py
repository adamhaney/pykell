from unittest import TestCase

from .types import expects_type, returns_type, PykellType, T


@expects_type(a=int, b=str)
def example_kw_arg_function(a, b):
    return a, b


class ExpectsTests(TestCase):
    def test_correct_expectations_kw(self):
        self.assertEqual(example_kw_arg_function(a=1, b="baz"), (1, "baz"))


@returns_type(int)
def add(x, y):
    return x + y

@returns_type(str)
def bad_add(x, y):
    return x + y


class ReturnTests(TestCase):
    def test_returns_type_positive(self):
        self.assertEqual(add(x=1, y=2), 3)

    def test_returns_type_negative(self):
        with self.assertRaises(TypeError):
            bad_add(x=1, y=2)


class TypeClassTests(TestCase):
    def test_type_enforcement_positive(self):
        str_type = PykellType(str)
        self.assertTrue(str_type.validate("abc"))

    def test_type_enforcement_negative(self):
        str_type = PykellType(str)
        with self.assertRaises(TypeError):
            str_type.validate(27)

    def test_data_enforcement_positive(self):
        z_string = PykellType(str, lambda d: d.startswith('z'))
        self.assertTrue(z_string.validate('zab'))

    def test_data_enforcement_negative(self):
        z_string = PykellType(str, lambda d: d.startswith('z'))
        with self.assertRaises(TypeError):
            z_string.validate('abc')

    def test_multiple_types_positive(self):
        """
        make sure we can add two types to the class and that it then
        says an object having one of those types is valid
        """
        str_int_type = PykellType(int)
        str_int_type.contribute_type(str)

        self.assertTrue(str_int_type.validate(2))
        self.assertTrue(str_int_type.validate("boo"))

    def test_multiple_types_negative(self):
        str_int_type = PykellType(int)
        str_int_type.contribute_type(str)

        with self.assertRaises(TypeError):
            str_int_type.validate(2.0)

    def test_multiple_validators_positive(self):
        a_z_type = T(str, lambda d: d.startswith('a'))
        a_z_type.contribute_validator(lambda d: d.endswith('z'))

        self.assertTrue("abcdz")

    def test_multiple_validators_negative(self):
        a_z_type = T(str, lambda d: d.startswith('a'))
        a_z_type.contribute_validator(lambda d: d.endswith('z'))

        with self.assertRaises(TypeError):
            a_z_type.validate("abc")
            
    def test_pipe_multi_type_syntax(self):
        str_int_type = T(int) | T(str)

        self.assertTrue(str_int_type.validate(2))
        self.assertTrue(str_int_type.validate("boo"))

class PykellContributionTests(TestCase):
    def setUp(self):
        self.positive_even_number = T(int, lambda d: d > 0) | T(float, lambda d: d % 2 == 0)

    def test_postive_float_is_valid(self):
        self.assertTrue(self.positive_even_number.validate(2.0))

    def test_positive_integer_is_valid(self):
        self.assertTrue(self.positive_even_number.validate(4))

    def test_negative_float_is_invalid(self):
        with self.assertRaises(TypeError):
            self.positive_even_number.validate(-4.0)

    def test_negative_int_is_invalid(self):
        with self.assertRaises(TypeError):
            self.positive_even_number.validate(-4)

    def test_odd_float_is_invalid(self):
        with self.assertRaises(TypeError):
            self.positive_even_number.validate(3.0)

    def test_odd_int_is_invalid(self):
        with self.assertRaises(TypeError):
            self.positive_even_number.validate(3)

                        
