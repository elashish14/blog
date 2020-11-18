Title: Structured Datatypes in Python
Date: 2020-11-10T21:42:48+00:00
Category: Computers
Tags: Software, Python
Slug: structured-datatypes-in-python

Any useful programming language provides a means to implement [composite data types][composite_data_types], ie. data types built as a composition of primitive and other composite data types. Python provides many ways to implement these structures, but I want to write about how to do this using [named tuples][1] and [dataclasses][2].

The reason why I like these two features is because they significantly improve the maintainability of a codebase. They very clearly declare all the fields a structure contains, and they integrate very nicely with Python's [type hints][type_hints]. Additionally, they make it possible to refer to fields using their names (rather than using an index or some other kind of non-descriptive identifier), and they can be *immutable*. I won't get into the pros and cons of immutability (there's a good reference [here][4] for the interested reader), but in general, from the standpoint of maintainability, it's preferable to make data structures immutable whenever possible so it is easier to reason about the code.

# Demonstration

Suppose we wish to store a `Person` object in memory. We'll define the fields that we wish to store as `name`, `birthdate`, `occupation`, and a unique identifier `id`.

## NamedTuple

Here is how we can define our `Person` object using a named tuple:

    :::python
    from collections import namedtuple

    Person = namedtuple('Person', ['name', 'birthdate', 'occupation', 'id'])
    some_person = Person(
        name='John Doe', birthdate=date(2020, 11, 10), occupation='student',
        id=1)

Looks great, but what happened to the type hints?! It actually turns out that there is a separate syntax for doing this in the `typing` module:

    :::python
    from datetime import date
    from typing import NamedTuple, Union

    class Person(NamedTuple):
        name: str
        birthdate: date
        occupation: Union[str, None]
        id: int

    some_person = Person(
        name='John Doe', birthdate=date(2020, 11, 10), occupation='student',
        id=1)

This approach satisfies all the criteria we outlined in the introduction. It provides type hints, it's immutable and it always guarantees that there are 4 fields that can be identified by name. What I like even more about this code is that anyone can see exactly what fields a `Person` structure contains by looking at its definition.

It is also possible to add methods to the class; for example:

    :::python
    class Person(NamedTuple):
        # field names here...

        def say_name(self):
            return f"My name is {self.name}"

Now we can run something like `print(some_person.say_name())`, and the logic for `say_name()` is inside the class, rather than in a function somewhere outside and far away.

It is also very easy to add fields to this structure. So long as the fields are always referred to by name, more fields can be added at will, and tools like `grep` can be used to easily find everywhere a particular field is used.

Here are some drawbacks to this method:

1. It is still possible to access fields by index. For example, this works:

        :::python
        birthdate = some_person[1]

    However, this would break if fields were added to the top of the class. For example, if an `address` field were added between `name` and `birthdate`, then the above code would have to be changed because the `birthdate` would now store the value of the address instead.

2. To the best of my knowledge, it is not possible to introduce a subclass of structures defined as named tuples. Of course, it is always possible to create another class composed of this structure.

## Dataclass

Data classes are very similar to named tuples. The syntax here is:

    :::python
    from dataclasses import dataclass
    from datetime import date
    from typing import Union

    @dataclass(frozen=True)
    class Person:
        name: str
        birthdate: date
        occupation: Union[str, None]
        id: int

    some_person = Person(
        name='John Doe', birthdate=date(2020, 11, 10), occupation='student',
        id=1)

It has all the same benefits mentioned above for named tuples, with the caveat that dataclasses are mutable by default (hence the `frozen=True` option). Additionally, dataclasses do not suffer from the two drawbacks listed above. It is not possible to refer to the fields by index, and a subclass of `Person` can be written like so:

    :::python
    class Employee(Person):
        salary: int

    some_employee = Employee(
        name='John Doe', birthdate=date(2020, 11, 10), occupation='student',
        id=1, salary=3000)

# Conclusion

Named tuples and dataclasses appear to serve the same purpose, so how to choose between them? A good breakdown of the small but important differences can be found [here][5]. The main difference is:

* Named tuples are backed by tuples, meaning they inherit most, if not all, of the properties of tuples. In other words, they are hashable (so they can be used as keys in dicts), orderable, immutable, etc.

* Dataclasses are backed by dicts, but have many options which determine what other things they can do. They can be made mutable or immutable, they can be made hashable, comparable, etc. depending on what options are passed to the `@dataclass` decorator.

Another important point to note is that dataclasses were introduced in Python 3.7, while named tuples go all the way back to Python 2.6, so if compatibility with older versions of Python is a concern, it is better to use named tuples.

[1]: https://docs.python.org/3/library/collections.html#collections.namedtuple
[2]: https://docs.python.org/3/library/dataclasses.html
[type_hints]: https://docs.python.org/3/library/typing.html
[4]: https://ocaml.xyz/book/convention.html#pure-vs.-impure
[5]: https://stackoverflow.com/questions/51671699/data-classes-vs-typing-namedtuple-primary-use-cases
[composite_data_types]: https://en.wikipedia.org/wiki/Composite_data_type
