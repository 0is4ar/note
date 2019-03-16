# shell.c

main调用run(parsecmd(buf))

parsecmd:
cmd = parseline(&s, es);

parseline:
cmd = parsepipe(ps, es)

parsepipe:
cmd = parseexec(ps, es0)
or
cmd = pipecmd(cmd, parsepipe(ps, es))


mkcopy(a,b): copy str between pointer a and b

