# bash\_tutorial

## Variables

`unset username` means delete variable `$username`

`local local_var = "haha"` means declare a variable local to a single function

### Exvironment variables

**Environment varables** are valid in **current shell session** `export GLOBAL_VAR="haha"`

### Positional parameters

| param | description |
| :--- | :--- |
| $0 | Script's name |
| $1 - $9 | parameter list elements |
| $\* or $@ | All \`positional parameters except $0 |
| $\# | The number of parameter, not counting $0 |

```text
$$
Shell本身的PID（ProcessID）
$!
Shell最后运行的后台Process的PID
$?
最后运行的命令的结束代码（返回值）
$-
使用Set命令设定的Flag一览
$*
所有参数列表。如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。
$@
所有参数列表。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。
$#
添加到Shell的参数个数
$0
Shell本身的文件名
```

## expansions

`echo beg{i,a,u}n` begin began begun

```text
echo {0..5} 
0 1 2 3 4 5
```

```text
echo {00..8..2}
00 02 04 06 08
```

this actually means from 00 to 08 using step size of 2

### Arithmetic expansion

has to be encapsuleted by $\(\(\)\)

result=$\(\( 5+2 \)\)

### Double and single quotes

variable name in double quotes will be replaced by its value while that in single quotes not

```text
echo "Your home: $HOME" # Your home: /Users/<username>
echo 'Your home: $HOME' # Your home: $HOME
```

variable having space:

if without double quotes, the system will **just** replace the variable with its value. With double quotes, tells the system it's actually **A** varieable

```text
echo "Your home: $HOME" # Your home: /Users/<username>
echo 'Your home: $HOME' # Your home: $HOME
```

## Array

Two ways of definign an array

```text
fruits[0]=Apple
fruits[1]=Pear
fruits[2]=Plum
```

`fruits=(Apple Pear Plum)`

also, two symbols used for expansion

```text
echo ${fruits[*]} # Apple Pear Plum
echo ${fruits[@]} # Apple Pear Plum
```

shell also have `%s`

```text
printf "+ %s\n" "${fruits[@]}"
# + Apple
# + Desert fig
# + Plum
```

slice ${fruit\[@\]:1:2}

## list of commands

| command | meaning |  |  |
| :--- | :--- | :--- | :--- |
| cmd1 ; cmd2 | cmd2 after cmd1 |  |  |
| cmd1 && cmd2 | cmd2 if cmd succeed |  |  |
| cmd1 |  | cmd2 | cmd2 if cmd unsucceed |

## conditional statements

single square brackets and double square brackets are almost the same, while double is more "modern", single is more compatible

### working with the file system

| param | meaning |
| :--- | :--- |
| \[ -e FILE \] | exist |
| -f | exist and regular file |
| -d | directory |

### binary operators

| param | meaning |
| :--- | :--- |
| \[ arg1 -eq arg2 \] | equal to |
| -ne | Not Equal |
| -lt | Less Than |
| -le | Less than or Equal to |
| -gt | Greater Than |
| -ge | Greater than or Equal to |

### other

| operation | effect |
| :--- | :--- |
| \[ ! EXPR \] | True if EXPR is false |
| \[ EXPR1 -a EXPR2\] | and |
| \[ EXPR1 -o EXPR2\] | or |

## pipe something

