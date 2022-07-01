"Disable compatibility with vi which can cause unexpected issues
"
set nocompatible
set rnu

" Enable type file detection. Vim will be able to try to detect the type of file in use.
filetype on

" Enable plugins and load plugin for the detected file type.
filetype plugin on

" Load an indent file for the detected file type.
filetype indent on

" Turn syntax highlighting on.
syntax on

" Add numbers to each line on the left-hand side.


" Enable auto completion menu after pressing TAB.
set wildmenu
" Make wildmenu behave like similar to Bash completion.
set wildmode=list:longest

:imap ii <Esc>

let mapleader = ","
call plug#begin()
    Plug 'preservim/NERDTree'
    Plug 'neoclide/coc.nvim', {'branch': 'master', 'do': 'yarn install --frozen-lockfile'}
    Plug 'vim-airline/vim-airline'
    Plug 'rafi/awesome-vim-colorschemes'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'tribela/vim-transparent'
    Plug 'jiangmiao/auto-pairs'
    Plug 'alvan/vim-closetag'    
    Plug 'junegunn/fzf'
    Plug 'junegunn/fzf.vim'
    Plug 'scrooloose/nerdcommenter'
    Plug 'yggdroot/indentline'
call plug#end()


nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <leader>r :NERDTree<CR>
nnoremap <leader>t :NERDTreeToggle<CR>
nnoremap <leader>f :NERDTreeFind<CR>
noremap <leader>fs :Files<cr>

" Wildmenu will ignore files with these extensions.
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx
set expandtab
set tabstop=4
set softtabstop=4
colorscheme molokai
set shiftwidth=4
set autoindent
set textwidth=80

