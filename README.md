pykell
======

This project is an experiment in bringing a
[recursive](http://en.wikipedia.org/wiki/Recursive_type),
[algebraic](http://en.wikipedia.org/wiki/Algebraic_types), [optional
type
system](http://en.wikipedia.org/wiki/Type_system#Optional_type_systems)
to python.

The idea behind this library was that if we allowed developers to be
more explicit in their expectations when they wrote code that they
would be able to help other developers avoid bugs that crop up during
the usageage of dynamic programming languages.

This type system borrows heavily from
[Haskell](http://www.haskell.org/haskellwiki/Haskell) and comes
packaged with the idea that the type system should help the developer
express their ideas.

TODO
----
  - Allow recursive type definitions
  - Change from using a .validate method to using having __call__ return a proxy model, similar to Mock
