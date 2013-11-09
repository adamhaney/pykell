from unittest import TestCase

from .types import expects_type, returns_type, make_type


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
        self.assertRaises(bad_add(x=1, y=2))


class TypeClassTests(TestCase):
    def test_type_enforcement_positive(self):
        str_type = PykellType(str)
        self.assertTrue(str_type.validate("abc"))

    def test_type_enforcement_negative(self):
        str_type = PykellType(str)
        self.assertTrue(str_type.validate(27))
