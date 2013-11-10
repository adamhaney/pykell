pykell
======

experiments in bringing elements of Haskell to python.

TODO
----

This isn't doing anything too interesting yet, more interesting things would be.

  - Factories for creating unions of types (ie Number = make_type((int, float, Decimal))
  - Factories for adding data validation to a type (ie PositiveNumber = make_type(Number, lambda datum: datum > 0)
  - Be able to pass PykellTypes into PykellTypes
  - Be able to chain | operators so types requirements can be or'd