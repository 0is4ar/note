# uniq2

```c
#include "types.h"
#include "stat.h"
#include "user.h"

char buf[1024];

void
uniq(int fd)
{
   int n;
 //   char *p, *q;
    n = read(fd, buf, sizeof(buf));
//    while((n = read(fd, buf, sizeof(buf))) > 0)
    char *p = buf, *a, *q, *r;
    while((a = strchr(p, '\n')) != 0)
    {
        *a = '\0';
        q = a+1;
        while((r = strchr(q, '\n')) != 0)
        {
            *r = '\0';
            if(strcmp(q,p) == 0)
            {
                memmove(q, r+1, n);
                r = q-1;
            }
            if(a != r)
            {
                *r = '\n';
            }
            q = r+1;
        }
        *a = '\n';
       p = a+1;
    }
    write(1,buf,sizeof(buf));
} 

/*
char*
readline(char *s)
{
    buffer[512]
    char *p;
    int i=0,c;
    while(1)
    {
        c=s[i];
        if (c<0)
        { 
            return NULL;
        }
        else if (c >= ' ' && i < BUFSIZE - 1) 
        {
            buffer[i ++] = c;
        }
        else if (c == '\n' || c == '\r') 
        {
            buffer[i] = '\0';
            return buffer;
        }
    }
}
*/

int
main(int argc, char *argv[])
{
  int fd, i;

  if(argc <= 1){
    uniq(0);
    exit();
  }

  for(i = 1; i < argc; i++){
    if((fd = open(argv[i], 0)) < 0){
      printf(1, "uniq: cannot open %s\n", argv[i]);
      exit();
    }
    uniq(fd);
    close(fd);
  }
  exit();
}
```

## adjunct with memmove

```c
#include "types.h"
#include "stat.h"
#include "user.h"

char buf[1024];

void
uniq(int fd)
{
   int n;
 //   char *p, *q;
    n = read(fd, buf, sizeof(buf));
//    while((n = read(fd, buf, sizeof(buf))) > 0)
    char *p = buf, *a, *r;
    while((a = strchr(p, '\n')) != 0)
    {
        *a = '\0';
        while((r = strchr(a+1, '\n')) != 0)
        {
            *r = '\0';
            if(strcmp(a+1,p) == 0)
            {
                memmove(a+1, r+1, n);
            }
            else
            {
                *r = '\n';
                break;
            }
        }
        *a = '\n';
       p = a+1;
    }
    write(1,buf,sizeof(buf));
} 

/*
char*
readline(char *s)
{
    buffer[512]
    char *p;
    int i=0,c;
    while(1)
    {
        c=s[i];
        if (c<0)
        { 
            return NULL;
        }
        else if (c >= ' ' && i < BUFSIZE - 1) 
        {
            buffer[i ++] = c;
        }
        else if (c == '\n' || c == '\r') 
        {
            buffer[i] = '\0';
            return buffer;
        }
    }
}
*/

int
main(int argc, char *argv[])
{
  int fd, i;

  if(argc <= 1){
    uniq(0);
    exit();
  }

  for(i = 1; i < argc; i++){
    if((fd = open(argv[i], 0)) < 0){
      printf(1, "uniq: cannot open %s\n", argv[i]);
      exit();
    }
    uniq(fd);
    close(fd);
  }
  exit();
}
```

