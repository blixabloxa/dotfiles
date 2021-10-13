" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " File Explorer
    Plug 'scrooloose/NERDTree'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    " Color previews for CSS  
    Plug 'ap/vim-css-color' 
    " VimWiki
    Plug 'vimwiki/vimwiki'
    " Gruvbox Clour Theme
    Plug 'morhetz/gruvbox'
    " Lightline:Status Bar
    Plug 'itchyny/lightline.vim'
    " Status bar icons
    Plug 'kyazdani42/nvim-web-devicons'

call plug#end()
