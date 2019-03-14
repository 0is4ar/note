# shell

`${pathname:(-4)}` means last for characters in $pathname

```

string='one_two_three_four_five'
remainder="$string"
first="${remainder%%_*}"; remainder="${remainder#*_}"
second="${remainder%%_*}"; remainder="${remainder#*_}"
third="${remainder%%_*}"; remainder="${remainder#*_}"
fourth="${remainder%%_*}"; remainder="${remainder#*_}"

```

## IFS

IFS (Internal Field Separator) is a special variable in shell

Create a text file called /tmp/domains.txt as follows:

```
cyberciti.biz|202.54.1.1|/home/httpd|ftpcbzuser
nixcraft.com|202.54.1.2|/home/httpd|ftpnixuser
```

Create a shell script called setupapachevhost.sh as follows:

```shell
#!/bin/bash
# setupapachevhost.sh - Apache webhosting automation demo script
file=/tmp/domains.txt

# set the Internal Field Separator to |
IFS='|'
while read -r domain ip webroot ftpusername
do
        printf "*** Adding %s to httpd.conf...\n" $domain
        printf "Setting virtual host using %s ip...\n" $ip
        printf "DocumentRoot is set to %s\n" $webroot
        printf "Adding ftp access for %s using %s ftp account...\n\n" $domain $ftpusername
	
done < "$file"
```


### another example
this example uses `<<<` instead of `<`
`IFS='_' read -r a second a fourth a <<<"$string"`