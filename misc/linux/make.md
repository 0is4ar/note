# make

basic rule of make:

C : D

B : C

A : B

when type `make A` in command line

make tries to find out how to compile B  
then C  
then D,  

if D exists in the directory, start to compile as the way it told to do  
OR error raised