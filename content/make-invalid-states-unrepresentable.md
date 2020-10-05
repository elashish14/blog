Title: Make Invalid States Unrepresentable
Date: 2020-10-05T19:22:39+00:00
Category: Computers
Tags: Software
Slug: make-invalid-states-unrepresentable

I just read a [fantastic article][1] about the "Make Invalid States
Unrepresentable" principle. I have never heard of this principle by name, but I
have seen code several times which violates this principle and it makes reading
and understanding it incredibly more difficult.

To quickly summarise this article, the core principle states that data in a
program should be structured in such a way that it should be impossible to have
invalid states in memory. As an example, if a series of time periods should be
expressed in a manner that prevents gaps and overlaps, one might be tempted to
use a representation of the form `List[(start: date, end: date)]`. However, if
the end of the current period does not match the start of the subsequent
period, then it is possible for gaps or overlaps to occur. If the data are
instead represented as `Set[(start: date)]` instead, with the implication that
the end date of that period is simply the next timestamp in order, then it is
impossible to represent a state with non-contiguous periods.

Why is this principle important? Because having redundant information in memory
makes it possible to surreptitiously introduce bugs. Simply looking at the data
representation of the `List` demonstrates that it is possible for gaps or
overlaps to occur, while looking at the `Set` representation *guarantees* that
it cannot. The `Set` representation precludes an entire class of bugs, while
the `List` representation invites them with warm, welcome arms. The only way to
ensure the memory is in a consistent state is to either audit the code
thoroughly to ensure that it never becomes inconsistent. It is the onus of the
code which encapsulates the data to ensure that the `List` provides the same
guarantee that the `Set` does.

Or, you could just trust that the code works, but please don't ever do that. It
will bite you, or whoever is responsible for maintaining that code, at the
worst possible time.

Of course, it would be remiss to write off the `List` representation as having
no advantages over the `Set` representation. Consider, for example, a function
to determine the length of a given period. In the case of the `List`, simply
locate the element and compute the difference between the start and end dates.
But the `Set` representation is more complicated. The logic for finding the
next element may be non-trivial, and could be more complex computationally as
well - `O(log(n))` if backed by a binary tree, or `O(n)` if backed by a
hashmap.

This is certainly bad, but not the end of the world. Often, developers choose
to structure their memory representations in a particular way because it makes
writing the code easier, even if it allows such invalid states where the memory
could violate the constraints of the system. But I still think that it is
better to write code such that the memory representation is simple, even if the
code representation is more complex.

This is because of another drawback of invalid states: writing tests to handle
and/or prevent these invalid states. The number of tests needed to cover all
states increases multiplicatively with the number of states (or state
categories), so many, many more tests must be written to ensure that the memory
stays consistent.

So in short, I think this is an important principle to follow, but it certainly
introduces trade-offs. This is why software is an engineering endeavour. There
are no perfect answers, and sometimes there is no solution that is optimal in
all respects. But I do think that following this principle goes a long way to
making a codebase easier to understand and validate.

[1]: https://kevinmahoney.co.uk/articles/applying-misu/
