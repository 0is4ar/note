# php\_session

client send **PHPSESSIONID** in cookie to server

server use PHPSESSIONID, gets a dictionary, $\_SESSION

## session\_set\_save\_handler

`bool session_set_save_handler ( callable $open , callable $close , callable $read , callable $write , callable $destroy , callable $gc )`

the most important two handlers are $read and $write

read is how session "get" the array using session ID write is how and where to save the array after modify \(several modificatiosn will be saved after the client go offline\) but I don't know how server know client lose connection since http is conn-less

## str

### compoare

#### with integer

only when the start of a string is "numeric chr" like "123abc", the string can be compared with integer "123abc" &gt; 121 will return true

#### with str

* if two string have the same length compare characters in two strings one by one, once there's a character is not equal, return "aabaa" &gt; "aaazz"
* if two string have different length compare the length

### strcmp

strcmp comsumes two parameters are string, return 0 if equal, others if unequal, like

```php
strcmp('a','z') #-25
strcmp('z','a') #25
```

if we pass into a array and string, it will also return 0

```php
$a = array('a' => 'b');
if(!strcmp('z',$a)){
    echo "haha";
    }
```

in this code, haha will be printed

