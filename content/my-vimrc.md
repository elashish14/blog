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


