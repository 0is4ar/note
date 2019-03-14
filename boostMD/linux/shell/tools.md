# shell

## ls

- `ls -lc`: sort by ctime

## alias

alias t1="tree -L 1"


## tree

tree -h 

![bc9fd825.png](:storage/6f27d652-ad8e-443f-9d94-0f0bb1560013/525e141b.png)


tree -L
level 

## grep


### invert match

-v 

## awk

---


### awk


```
1 haha boom
2 haha boom
```

#### print 

- `awk '{ print $1 $3 }'`

result:

1 boom\
2 boom

##### -F

use -F to specify the separtor 

like:

`awk -F, '{ print $1 $3 }' `

to split following thins:

```
1,haha,boom
2,hehe,buuu
```


## fg

`jobs` can see background jobs
and use `fg %1` can take job 1 to foreground

## cut 

`cut -d "/" -f 3`
is equal to `.split('/')[2]`