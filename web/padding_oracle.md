# padding_oracle

the padding oracle attack based on several assumption

we pass ciphertext to sever 

1. First, server decipher the ciphertext, there will be three different results:
    padding error, plaintext is wrong, plaintext is correct
    And the ruturn content of the padding error should be different from the other two.

2. the first block of ciphertext can't be cracked

## crack

![](_v_images/20190111180822167_384099137.png =430x)

For the last byte of Block n, there are two situations

1. Block n has exactly 16bytes
2. the last byte of Block n is 0x01

both these two situations server will not return bad padding

We change the last byte of Block n-1, until the server doesn't return bad padding, at this time, the last byte of Block n-1 is X

then we can use 0x01 ^ X = last Intermediate Byte of Block n

In this way, we can guess out the last bytes of Block n
Then, we can guess the second last byte by assuming the last two bytes of Block n are 0x02 0x02.

After we get all intermediate bytes of Block n,

Ciphertext(block n-1) ^ Intermediate Bytes(block n) =    
the plantext of block N   
(just like the last step of normal decipher block n)

