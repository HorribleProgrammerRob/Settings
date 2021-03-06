set tabstop=4		" Set tabstop to tell Vim how many columns a tab counts for. 

set softtabstop=4	" Set softtabstop to control how many columns vim uses when you hit Tab in insert mode. 
					" If softtabstop is less than tabstop and expandtab is not set, vim will use a combination of tabs and
					" spaces to make up the desired spacing. If softtabstop equals tabstop and expandtab is not set, vim will
					" always use tabs. When expandtab is set, Vim will always use the appropriate number of spaces.

set shiftwidth=4	" Set shiftwidth to control how many columns text is indented with the reindent operations (<< and >>)

set expandtab		" When expandtab is set, hitting Tab in insert mode will produce the appropriate number of spaces.

syntax on
set nu

colorscheme happy_hacking

set laststatus=2

set rtp+=/usr/local/lib/python3.6/dist-packages/powerline/bindings/vim
set laststatus=2
set t_Co=256
