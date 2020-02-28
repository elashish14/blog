Title: My .vimrc File
Date: 2020-01-18T22:20:20+00:00
Category: Computers
Tags: Software, Vim
Slug: my-vimrc

Behold, my .vimrc file!

    :::vimscript
    set nojoinspaces
    set bg=dark
    set sw=2
    set ts=2
    set sts=2
    set ruler
    set ffs=unix
    map Q q
    map q: :
    map Y y$

    let g:leave_my_textwidth_alone=1
    let g:python_recommended_style=0
    set expandtab
    set nojoinspaces
    set hlsearch
    set ffs=unix
    set bs=indent,eol,start
    map Q q
    map q: q
    map Y y$
    nmap K k
    syntax on
    set ruler
    set showmode

    if has("gui_running")
      colorscheme elflord
    endif

    set t_Co=256

    highlight ExtraWhitespace ctermbg=lightred guibg=lightred
    autocmd VimEnter,InsertEnter * syn match ExtraWhitespace /\s\+$/ containedin=ALL

    highlight Tabs ctermbg=lightgreen guibg=lightgreen
    autocmd VimEnter,InsertEnter * syn match Tabs /\t/ containedin=ALL

I have tried several editors over a few short years, but I feel most
comfortable doing my development in vim. The ease of navigation and power of
editing is virtually unmatched in my opinion. I can remember most of these by
heart, but the only ones I need to look up are the last 4 lines. To see what
they do, read [this article][1].

But surprisingly, there are no plugins or other complicated configuration here.
I find vim extremely powerful, even with little to no configuration.
I like this very much - because when I ssh into a new server, or am working on
someone else's computer, I still have a consistent, familiar environment
without the need for several minutes/hours of setup. But in case I ever do need my full configuration - well, here it is, I suppose.

[1]: vim-extra-whitespace.html
