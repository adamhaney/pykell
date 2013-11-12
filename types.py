class T(object):
    """
    A pykell 'type' class. This is different from a python type in
    that it allows a type to be the union of multiple types and allows
    for data validation to be baked into the type.

    This allows us to create types for things like, 'even_positive_number'

    >>> even_positive_number = T(int, lambda d: d > 0) | T(float, lambda d: d % 2 == 0)
    """

    def __init__(self, type_=None, validator=None):
        if type_:
            self.types = [type_]
        else:
            self.types = []
        if validator is not None:
            self.validators = [validator]
        else:
            self.validators = [lambda d: True]

    def validate(self, var):
        valid_type = False
        for type_ in self.types:
            if isinstance(var, type_):
                valid_type = True

        # If we don't have a type skip type validation
        if len(self.types) == 0:
            valid_type = True
                
        if not valid_type:
            raise TypeError(
                "expected object of type {}, received {}".format(
                    ",".join([str(t) for t in self.types]),
                    type(var)
                )
            )

        for validator in self.validators:
            if not validator(var):
                raise TypeError("'{}' falied the data validation".format(var))

        return True

    def contribute_type(self, type_):
        self.types.append(type_)

    def contribute_validator(self, validator):
        self.validators.append(validator)

    def contribute_pykell_type(self, pykell_type):
        for type_ in pykell_type.types:
            self.contribute_type(type_)

        for validator in pykell_type.validators:
            self.contribute_validator(validator)

        return self

    def __repr__(self):
        return u"#<pkell.types.PykellType {}, w/ {} validators>".format(self.types, 1)

    def __or__(self, rhs):
        return self.contribute_pykell_type(rhs)
        

def expects_type(**expectations):
    def _wrap(fn):
        def _expectation_checker(**kwargs):
            for arg, pykell_type in expectations.items():
                print arg, pykell_type
                pykell_type.validate(kwargs[arg])
            return fn(**kwargs)
        return _expectation_checker
    return _wrap


def returns_type(pykell_type):
    def _wrap(fn):
        def _expectation_checker(**kwargs):
            r = fn(**kwargs)
            pykell_type.validate(r)
            return r
        return _expectation_checker
    return _wrap
