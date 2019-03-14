# hash_extension(sha1)

sha1 works with block size 512 bits, block size less than 512 bits needs padding

the result of sha1 is 20 bytes

## how sha1 works

### high level

starts with five "registers" having **initial value**, they are  
67452301, EFCDAB89, 98BADCFE, 10325476, C3D2E1F0

then plaintext get in, block by block,  
block 1 calculate with 5 registers,  produce **5 new value in registers**  
block 2 calculate with 5 new registers, produce 5 new values again in those registers.
after calculation
Values remainning in regiesters are **result**

## how mac works 

mac stands for **message authentication codes**  

- client side  
when user want to input username  
have to input username and a mac, like
"admin","aoisdfjio238tjze890q2309j290f"

- server side  
server keep a **key**  
when receiving user input,  
sha1(concat(key,userinput)) is the mac 


### notice

if the input has a length of 5 blocks  
the key will only be added to the first block

## How to crack

if we want to change `{'username':'joe','admin':False}` to `{'username':'joe','admin':True}`  
assumes the length of key is 11  

1. first, we input `{'username':'joe','admin':False}`  
got a digest $hash_1  

2. Then, use my own python sha1 function,  
set the value in registers to $hash_1  
use this function to sha1  `{'username':'joe','admin':True}`  
then got result $hash_2

3. input $origin + padding_block_1 + $after_forge

padding bytes' format are "0x80 0x00 0x00 ... 0x00 0x00 0xA0"

### explaination

explain step 3

server side got the user input, divide it into 2 blocks,  
first add key to the first block, and do sha1,  
after the first block sha1, the value in 5 registers are exactly what we have in step 2  
so after sha1 the second block, the answer will be the same as $hash_2,
