class PykellType(object):
    def __init__(self, type_, data_test=lambda d: True):
        self.type_ = type_
        self.data_test = data_test

    def validate(self, var):
        if not isinstance(var, self.type_):
            raise TypeError("expected object of type {}, received {}")
        if not self.data_test(var):
            raise TypeError("'{}' falied the data validation".format(var))
        return True
        

def expects_type(**expectations):
    def _wrap(fn):
        def _expectation_checker(**kwargs):
            for arg, type_ in expectations.items():
                if not isinstance(kwargs[arg], type_):
                    raise TypeError(
                        "{} expected {} to be instance of {}, instead received {}".format(
                            fn.__name__,
                            arg,
                            type_,
                            type(kwargs[arg])
                        )
                    )
            return fn(**kwargs)
        return _expectation_checker
    return _wrap


def returns_type(type_):
    def _wrap(fn):
        def _expectation_checker(**kwargs):
            r = fn(**kwargs)
            if not isinstance(r, type_):
                raise TypeError(
                    "{} should have returned a value of {} instead it returned {}".format(
                        fn.__name__,
                        type_,
                        type(r)
                        )
                    )
            return r
        return _expectation_checker
    return _wrap
