Title: Static Website Generation
Date: 2019-01-20T22:24+00:00
Category: Computers
Tags: Software, Meta, WWW
Slug: static-website-generation

I created this website using [Pelican][1]. I think it's absolutely fantastic.
Pelican belongs to a class of software called static site generators. Static
site generators are pieces of software which allow users to write articles
using very simple markup languages such as [Markdown][2], or [Restructured
Text][3] and generate them into whichever output format is desired (typically
HTML, but potentially also other formats such as RSS/Atom, PDF, etc.).

Here are some reasons why I think this is the best way to write a personal
website:

1. It embodies the principle of separation of content and presentation. Or in
   other words, I can just focus on writing content and not have to worry about
   any styling or formatting. I feel that this is a crucial aspect of writing
   good content. It's not important to know how text is going to be formatted
   on a page while it is being written. If the output format is appropriate,
   the presentation of text can be adapted no matter what is written.

2. Output documents are just plain HTML that can be served easily by any HTTP
   server with essentially no configuration needed. I'm aware that it's 2019,
   but I still think the world-wide web was best when it was just a collection
   of information contained between hyperlinked HTML documents.

3. I don't need bloated, complex tools to write content. All that is necessary
   is a text editor (my favourite being [vim][4]) and a terminal.

4. I think it's the perfect paradigm for many classes of content-driven
   websites. HTML documents are difficult to write natively - the syntax is
   awful and it becomes difficult to keep links updated should they happen to
   change. Static site generators obviate the need for dynamically generated
   websites, which can require significant server-side resources and are
   difficult to configure and secure. However, they still don't rely on
   unnecessary and dangerous technologies like javascript either.

Of course, there are several alternatives to Pelican, such as [Hugo][5],
[Jekyll][6], and others. I prefer Pelican because most Linux systems come with
Python pre-installed, and I like how Python manages libraries and dependencies
using a virtualenv.

Overall, I think this is a great way to generate simple websites. It would be
great to see tools like this continue to catch on.

[1]: https://blog.getpelican.com/
[2]: https://daringfireball.net/projects/markdown/
[3]: http://docutils.sourceforge.net/rst.html
[4]: https://www.vim.org/
[5]: https://jekyllrb.com/
[6]: https://gohugo.io/
