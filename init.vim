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

" Display 5 lines above/below the cursor when scrolling with a mouse.
set scrolloff=5
" Highlight matching search patterns
set hlsearch
" Enable incremental search
set incsearch
" Include matching uppercase words with lowercase search term
set ignorecase
" Include only uppercase words with uppercase search term
set smartcase
" Enable auto completion menu after pressing TAB.
set wildmenu
" Make wildmenu behave like similar to Bash completion.
set wildmode=list:longest

:imap ii <Esc>
let mapleader = ","

call plug#begin()
    Plug 'preservim/NERDTree'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
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
    Plug 'ryanoasis/vim-devicons'
    Plug 'EdenEast/nightfox.nvim' " Vim-Plug

    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
call plug#end() 

let g:coc_global_extensions = [ 'coc-tsserver' ]
lua <<EOF
require'nvim-treesitter.configs'.setup {
  -- ensure_installed = "maintained", -- one of "all", "maintained" (parsers with maintainers), or a list of languages
  highlight = {
    enable = true,              -- false will disable the whole extension
  },
}
EOF
let g:airline_powerline_fonts = 1
" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)
let g:python_highlight_all = 1
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
colorscheme nightfox

set shiftwidth=4
set autoindent
set textwidth=80

