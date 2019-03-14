<!-- toc -->

- [tools](#tools)
  * [web_search](#web_search)
  * [the fuck](#the-fuck)
  * [sudo](#sudo)
  * [ranger](#ranger)
  * [fd](#fd)
  * [howdoi](#howdoi)
  * [glances](#glances)
  * [lazygit](#lazygit)
  * [wtf](#wtf)
  * [bat](#bat)
  * [tldr](#tldr)
  * [true color](#true-color)
  * [httpie](#httpie)
  * [curl cht.sh/tar](#curl-chtshtar)
  * [rg](#rg)
  * [fzf](#fzf)
    + [ctrl](#ctrl)

<!-- tocstop -->
# tools

## web_search

## the fuck

## sudo

## ranger

## fd

## howdoi

## glances

## lazygit

## wtf

personal information dashboard for terminal
## bat

## tldr
better man page

## true color

awk 'BEGIN{
 s="/\\\/\\\/\\\/\\\/\\\"; s=s s s s s s s s;
 for (colnum = 0; colnum<77; colnum++) {
 r = 255-(colnum*255/76);
 g = (colnum*510/76);
 b = (colnum*255/76);
 if (g>255) g = 510-g;
 printf "\\033\[48;2;%d;%d;%dm", r,g,b;
 printf "\\033\[38;2;%d;%d;%dm", 255-r,255-g,255-b;
 printf "%s\\033\[0m", substr(s,colnum+1,1);
 }
 printf "\\n";
}'

## httpie

manual http request

## curl cht.sh/tar

or 

curl cht.sh/languagename/questions

## rg

## fzf

vim `fzf`

use ctrl+j/k 

cd **<tab>

vim **<tab>
cd **<tab>


kill -9 <tab>

fzf --prefiew 'bat -100 {}'

fd * -t file|fzf

> `fd -t file` means type file

### ctrl

ctrl-t will paste selected filename on command line

ctrl-r paste from history

alt-c cd into
