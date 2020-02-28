Title: Highlighting and Deleting Extra Whitespace in Vim
Date: 2020-02-28T22:41:44+00:00
Category: Computers
Tags: Software, Vim
Slug: vim-extra-whitespace

Here is a very helpful but difficult-to-remember portion of configuration
taken from my .vimrc file:

    :::vimscript
    highlight ExtraWhitespace ctermbg=lightred guibg=lightred
    autocmd VimEnter,InsertEnter * syn match ExtraWhitespace /\s\+$/ containedin=ALL

    highlight Tabs ctermbg=lightgreen guibg=lightgreen
    autocmd VimEnter,InsertEnter * syn match Tabs /\t/ containedin=ALL

# The Rationale

The above lines help in highlighting whitespace in vim. Extraneous whitespace
at the end of a line is the bane of many developers' existence. These
superfluous whitespace characters make editing difficult and also screw up
diffs when examining patches and version control. For example, pressing `A` in
normal mode in vim will enter insert mode at the end of the current line that
the cursor is on (try it!). However, if there is additional whitespace at the
end of the line, the cursor will not go to the end of the line, but it will go
to the end of the whitespace, forcing the user to delete all the additional
characters before beginning an insert.

Additionally, developers should **always** be aware of whether their code is
using tabs or whitespace for indentation, in order to preserve consistent code
appearance. I have seen plenty of Java code which appears like so:

    :::java
    public static void main(String args[]) {
        System.out.println("Hello world!");
            return 0;
    }

These sorts of situations appear very frequently when developers mix tabs and
spaces for indentation (another bane of programmers' existence). It would even
be a syntax error in Python.

What makes fixing these whitespace inconsistencies even more vexing is the
fact that users must create a special commit to correct them. However, this
screws up the version control history because tools like `git blame` and `git
log` will now include references to commits which fix the whitespace
inconsistencies, rather than references to when the code was actually written.
This makes tracing and fixing bugs significantly more annoying.

# The Diagnosis

The `highlight` command creates a highlight named `ExtraWhitespace` and declares
the colors associated with it. For this, I chose to make the background colour
`lightred`.

The `autocmd` command states that on the actions `VimEnter,InsertEnter` on
files matching `*` (ie. any name), vim should perform the `syn` command which follows. The `syn` command matches the `ExtraWhitespace` highlight to portions of the text which match the proceeding regex `/\\s\+$/` - this regex means all whitespace up to the end of a line.

This means that when the editor detects extra whitespaces, the character will be marked and easily visible for the user to see. The second set of commands repeats the process. This time, tab characters visible anywhere in the document will be highlighted `lightgreen`.

# The Solution

And how do we actually remove the whitespace inconsistencies? To remove extra
whitespace at the end of our lines, we can run:

    :::vimscript
    :%s/\s\+$//

This is a simple search and replace - `\s\+$` matches space characters at the
ends of lines, and the replacement is obviously the empty string.

In my projects, I usually use 2 or 4 whitespaces for indentation, and never
use the `tab` character. So in my `.vimrc`, I have

    :::vimscript
    :set expandtab

And then to replace the tabs with spaces, we can simply run

    :::vimscript
    :retab

All tabs will be expanded and replaced with the appropriate amount of spaces.
Usually, this means that I also have something like this set in my .vimrc:

    :::vimscript
    :set ts=4

This means that tabstops are set to 4 spaces, which is the amount of space a
tab will be expanded to. For more information, see `:help retab`.

This obviously breaks Makefiles. Fortunately, I don't have to write them
frequently. And in my honest opinion, nobody should ever need to manually
write a Makefile these days (with infrequent exceptions), but that is a
separate article.

# Next Steps

Many other editors provide a means to perform this automatically, but this is
a very simple way to do it in vim. Most developers do not visualise whitespace
characters in their editors, because editors do not enable it by default, or
because they feel that it adds too much visual noise. However, I feel that
being aware of whitespace characters in a software project is important, and
amongst other formatting habits, if good practices are established early in
the project, then it will provide benefits and prevent headaches later on.
