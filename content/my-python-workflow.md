Title: My Python Workflow
Date: 2020-04-25T01:45:04+00:00
Category: Computers
Tags: Software, python, pdb, vim
Slug: my-python-workflow

Python is my favourite language. Some find it surprising that my preferred
editor for coding is not an IDE, but vim. Not even vim with plugins, but vim
with [very few customisations][1]. This won't be an in-depth post on how I use
vim - that would take me too long to write - but it will cover a couple small
tips.

First, I should note how useful I find [pdb][2]. `pdb` is the Python debugger -
you use it to trace errors and analyse variables. But the greatest power is
that you can use it to test new code as well. So frequently, I'll reach a point
in the code that I want to test as I write it. I'll put a simple line like
this:

    :::python
    import pdb ; pdb.set_trace()

You can put it almost anywhere in the middle of your code. Aside from analysing
variables and jumping through the stack, you can also write new statements. For
example, you can fiddle with a dict or list and modify the arguments being
passed to functions.

Technically this is possible in other languages (C, Java, etc.), and while they
are great at analysing memory and the stack, I find that they are not as
powerful at interpreting and running code on the fly.

At this point, I estimate that I write about 50% of my non-boilerplate code in
`pdb` and then just copy it from the interpreter into my source code. This
saves me a lot of time later debugging code that I wrote without testing. I
usually have `import pdb; pdb.set_trace()` stored in my `"d` register. You can
view your paste registers in vim by running

    :::text
    :reg d

which for me shows

    :::text
    :reg d
    Type Name Content
      l  "d   ^I^Iimport pdb ; pdb.set_trace()^J

so when I want to put in a breakpoint, I type

    :::text
    "d[P

This says "take the contents of register **"d** and **P**aste them on the line
above the cursor". The **[** tells vim to paste the text at the same level of
indentation that the cursor is currently present on, which is particularly
handy in Python.

From here, I just run my code in a separate terminal and wait until I hit the
breakpoint. Then inspect/test whatever I like, paste whatever code I write back
into the file when I'm done. Writing code this way prevents a lot of spelling
errors, type errors, syntax errors, and so on because these are caught as I'm
writing it in the interpreter. It is also very useful for testing functions in
libraries or elsewhere in the code. I find it to be a very powerful workflow.

[1]: my-vimrc.html
[2]: https://docs.python.org/3/library/pdb.html
