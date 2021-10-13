source $HOME/.config/nvim/vim-plug/plugins.vim

set number
set nohlsearch

let NERDTreeShowHidden=1
let g:vimwiki_list = [{'path': '~/vimwiki/', 'syntax': 'markdown', 'ext': '.md'}]

nmap <C-n> :NERDTreeToggle<CR>
