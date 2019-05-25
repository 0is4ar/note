## Three fuzzing styles 

### pure random fuzzing

### random mutation based on exsit 

For example, test PDF viewer, crawling a lot of PDF on the Internet,

Then, based on those PDF files, adding some random bytes, and feed viewer.

### Generation-based fuzz

basically have a skeleton of the file to feed the program to be tested. The skeleton ensure feeds are "valid"


For example, to test a website, the skeleton is some "basic" HTTP protocol structure that ensure feeding will not be discard at once.


**efficiency is a key of fuzz**

- fuzz a component of a big program.

    for example, want to fuzz png render of chrome, starting up chrome takes a lot of time. Instead, finding the library used by Chrome to render png, write a wrapper, fuzz the wrapper

    - but if the program is not open source, we are unable to find the libarary it uses, we could debug it, set breakpoint at the beginning of component, fork for every iteration.



## How to detect bugs


- crashed like SIGSEGV
- Check invariants
- Determine the severity or exploitability

Like buffer overflow of one byte, at most time, it won't crash the program but is still a "vulnerability"

There's a thing named "Sanitizeer" which is used during compiling and it makes program more fragile so that bugs are more detectable.


## Failures

- A lot of crashes are actually at the same point. 
- A lot of crashes are not exploitable.


## Code coverage

``` 

if (a > 2)
  a = 2;
if (b > 2)
  b = 2;

```

### Line coverage

How many lines are covered

(3,3) cover all lines


### branch coverage

using (3,3) to feed the program, we got 100% coverage in "line coverage"

However, we didn't manage to cover all brances.


We need to cover all branchs **instead** of cover all combination of brances.

(3,3) and (0,0) are enough


### Path Coverage

Cover all unique execution path

(0,0), (3,0), (0,3), (3,3)
