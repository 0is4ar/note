# flush

Normally output to a file or the console is buffered, with text output at least until you print a newline. The flush makes sure that any output that is buffered goes to the destination.

I do use it e.g. when I make a user prompt like Do you want to continue \(Y/n\):, before getting the input.

This can be simulated \(on Ubuntu 12.4 using Python 2.7\):

```text
from __future__ import print_function

import sys
from time import sleep

fp = sys.stdout
print('Do you want to continue (Y/n): ', end='')
# fp.flush()
sleep(5)
```

If you run this, you will see that the prompt string does not show up until the sleep ends and the program exits. If you uncomment the line with flush, you will see the prompt and then have to wait 5 seconds for the program to finish

There are a couple of things to understand here. One is the difference between buffered I/O and unbuffered I/O. The concept is fairly simple - for buffered I/O, there is an internal buffer which is kept. Only when that buffer is full \(or some other event happens, such as it reaches a newline\) is the output "flushed". With unbuffered I/O, whenever a call is made to output something, it will do this, 1 character at a time.

Most I/O functions fall into the buffered category, mainly for performance reasons: it's a lot faster to write chunks at a time \(all I/O functions eventually get down to syscalls of some description, which are expensive.\)

flush lets you manually choose when you want this internal buffer to be written - a call to flush will write any characters in the buffer. Generally, this isn't needed, because the stream will handle this itself. However, there may be situations when you want to make sure something is output before you continue - this is where you'd use a call to flush\(\).

