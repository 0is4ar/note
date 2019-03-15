# apache

## RewriteCond & RewriteRule

### example

RewriteCond %{REQUEST\_FILENAME} !-l

RewriteRule ^\(.+\)$ index.php?url=$1 \[QSA,L\]

### explaination

RewriteCond means "execute the next RewriteRule only if this is true"

the example means the request is not for a link

RewriteRole means if request match the regex,  
`/haha` will be rewritten as `/index.php?url=haha`

`QSA` means "Query String Append",  
for example,  
`/haha?a=1` will be changed to `/index.php?url=haha&a=1`

L means if the rule matches, don't process any more RewriteRules below this one.

