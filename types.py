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


def make_type(**expectations):
    pass