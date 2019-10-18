Title: Why I Prefer Document Typesetters
Date: 2019-10-17T01:40+00:00
Category: Computers
Tags: Software, Productivity
Slug: why-i-prefer-document-typesetters

I want to write a short post on why I feel that document typesetters are
advantageous to using document processors for generating publications. This is
not meant to be a persuasive essay. Rather, I just wanted to take a moment here
to comprehensively describe some technical reasons why I prefer this method.

Broadly speaking, there are two means of creating a document. *Document
processors* include such tools as LibreOffice Writer and Microsoft Word. Many
people, when faced with the task of preparing a document such as a letter,
report, or presentation, will immediately opt for one of these kinds of tools.
*Document typesetters* on the other hand, take as input a file or series of
files with some kind of markup syntax and generate documents from them.
Examples of document typesetters include [LaTeX][1] and [Sphinx][2]. Some
examples of markup systems include [Markdown][3] and [reStructuredText][4].

What follow are some of the reasons I prefer document typesetters.

## Declarative Structure

Document processors make direct formatting easy. This frequently encourages bad
behaviours, such as using direct formatting to structure section headers and
other document elements. On the other hand, typesetters encourage authors to
*declare* structural elements of the text and renders them automatically. For
example, declaring a section in LaTeX can be done by simply writing
`\section{Name of the Section}`.

Here are a few reasons why this is important:

*   If the author at some later point wishes to change the formatting of a
    section header (or some other stylistic element), the change will be
    applied automatically to all such declared elements.

*   A Table of Contents (or Figures or Tables) can be generated and updated
    automatically from these declarations.

*   Organizations which wish to impose a particular, consistent style can
    provide style files directly to authors, and authors can simply write
    content without having to focus on stylistic details. This can be
    particularly useful for academic journals or business organizations.
    Authors are relieved of having to worry about styling and can instead focus
    solely on the content they wish to convey.

*   The likelihood of a particular element being incorrectly formatted due to a
    user error is significantly diminished and this in turn gives the author
    more time to focus on writing content rather than manually fixing styling
    issues. A significant part of this issue is that fact that document
    processors rely on extremely complicated document formats. The next section
    will go into this point in more detail.

## Complexity of Document Formats

The [ODF][5] standard was spearheaded by the developers of the LibreOffice
suite (at the time when the project was known as OpenOffice.org), while
Microsoft led the standardization of the [OOXML][6] format (in a very
controversial manner one might recall). ODF is a somewhat complex (but still
well-designed) standard, and OOXML is an incredibly complex one - the standard
document itself is over [6000 pages][7]!

The use of document processors vs. document typesetters can be thought of in a
philosophical context. Document processors are applications designed around a
particular format. Users never interact with the document format itself, rather
they interact with an application which writes out to that document. Nobody
ever looks directly at the content of what is being stored.

Reasons like this are why subtle changes in formatting can go unnoticed.
Frequently, users will paste content which transparently inserts its own
formatting, or they will make an errant keystroke/mouse click that makes such a
change. If users looked directly at the document that's written, it would be as
obvious as seeing an errant `\textbf{}` in a LaTeX document. However, this is
not possible because the ODF and OOXML formats are too complicated to be
manipulated manually!

The point here is this: formatting errors can appear very transparently in
complex formats such as ODF and OOXML because users never look at the actual
data that they're creating - they're just looking at a very high level
abstraction of it when they are using their document processing software.
Markup languages, on the other hand, usually allow users to write their content
in simply structured Unicode files; and since users can see *exactly* what is
being passed to the document generator, they can rest assured that these types
of transparent errors do not occur.

## Flexibility of Conversion Tools

Another advantage of writing content in a markup language is that the document
can be viewed in multiple formats. This post, for example, is being  written in
Markdown, and I can easily generate HTML from it using
[pelican][9]. However, it can be trivially
converted into other formats as well such as PDF, roff/troff (the format used
by man pages), ODF, OOXML, or even other document formats such as TeX or
reStructuredText! A tool like [pandoc][8] demonstrates the power of this
capability to an extreme. It can convert the raw document content between
several types of document formats.

This is possible because the genius of typesetting is in the realization that
ultimately, a document is a fairly simple tree-like structure of document
elements. The vast majority of documents all consist of the same basic
structures: sections, subsections, text, tables, figures, numbered and
unnumbered lists, references, a couple other types of elements, and some
metadata such as the author, date, etc. As soon as a program can read this
information into its own syntax tree, it can be manipulated at will, converting
the content to and from different formats, each of which is appropriate for a
particular for whatever purpose is needed. The next section talks about how this flexibility in the use of the content can be useful in document preparation.

As an example of how this can enhance user productivity, a typesetter could be configured to generate different styling
One direct benefit of this is that
the typesetter can automatically generate separate documents for drafting,
review, and final publication.

## Separation of Software Responsibilities

A standard document processor must provide authors the means to perform all
tasks of the document generation process: writing, viewing, collaboration,
updating, archiving, and error checking. As a result, document
processors become a tool that is forced to do everything, and as a result, they
cannot do any of those tasks particularly well. By contrast, typesetters enable
a more distributed workflow, delegating each task of the process to a separate,
specialized tool.

### Writing

The markup languages which are usually read in by typesetting tools are usually
written in simple ASCII or Unicode text files. Thus, authors can use even the
most basic of text editors to write content. They can do it on a simple
machine, even one without a graphics server!

On the other hand, there are far fewer programs that can manipulate ODF or
OOXML files. All of them are considerably more complex and resource intensive
than a text editor. And when they crash, users often end up losing significant
amounts of work.

### Viewing

Collaborators who need to preview text in its distribution format can do so in
whichever medium they wish. The flexibility to view in a web browser or PDF
viewer is possible. It is also possible to output to multiple kinds of paper
formats if a hard copy is desired. Additionally, multiple styles can be created
and chosen dynamically. For example, separate styles could be created for
drafting, review, and final publication.

### Collaboration

To begin with, input documents can be split into multiple files, so multiple authors can work independently on their own sections without having to perform difficult manual merges at the end of the process or using manual labour to ensure that styling is consistent. If users wish to use an external tool to sync their changes (such as git, for example), they can easily share changes in isolated patches and rebase on the most recent working copy.

### Updating

Consider what might happen if someone realizes they made an error in a plot
that they generated for several documents. If they are all stored in ODF
format, the user must open each file, update it manually, and save it. Even
worse, suppose there are hundreds of files and it is not even known which ones
use said figure! The task quickly becomes impossible!

If the files were stored in a text-based format, it is easy to search which ones contain the figure by its filename. Then the user simply has to update the file in place and regenerate the documents that refer to it. It can be done very quickly and easily.

### Archiving

As insinuated in the previous section, it can become necessary to search
through several old documents for a particular string of text, or a reference
to a particular image. If the files are in a text-based format, searching becomes very simple. If they are stored in a large XML format such as an ODF, searching becomes much more difficult.

Another issue to consider is what might happen if there are multiple versions of a file on disk. A tool like diff (or vimdiff) can quickly tell the differences between the files, or a checksum can tell whether they are the same. However, if the document format is too complicated, it becomes much harder to tell how they are different, or if they are different at all! And once again, scalability becomes an issue; it becomes an arduous task if there are only a few versions, but if there are dozens, it becomes impossible to track.

### Error Checking

Tasks like spell checking are built into most document processors, but can also
be run externally. Extracting statistics like the number of spelling errors or
the level of vocabulary or the number of times a reference is used are easier
to implement and use when they can be as standalone programs outside of a
document processor.

## Conclusion

This is a mostly exhaustive list of my opinions about why I like document typesetters. Ultimately, there are trade-offs with every tool for a particular task, and I am of course not suggesting that documents should always be prepared in a particular way. But hopefully this post will stimulate thought on when, how and why it might be appropriate to do things somewhat differently.

[1]: https://www.latex-project.org/about/
[2]: https://www.sphinx-doc.org/en/master/
[3]: https://en.wikipedia.org/wiki/Markdown
[4]: https://en.wikipedia.org/wiki/ReStructuredText
[5]: https://en.wikipedia.org/wiki/OpenDocument
[6]: https://en.wikipedia.org/wiki/Office_Open_XML
[7]: http://www.ecma-international.org/news/PressReleases/PR_TC45_Dec2006.htm
[8]: https://pandoc.org/
[9]: static-website-generation.html
