# pull 部分

```text
$ git init <project>
$ cd <project>
$ git remote add origin ssh://<user>@<repository's url>
$ git config core.sparsecheckout true
$ echo "path1/" >> .git/info/sparse-checkout
$ echo "path2/" >> .git/info/sparse-checkout
$ git pull origin master
```

第一条命令git init ，先建立一个空的版本库，用实际的目录名替代。 第二条命令cd ，进入创建的新的版本库的目录。 第三条命令git remote add origin ssh://&lt;user&gt;@&lt;repository's url&gt;，添加远程库的地址。 第四条命令git config core.sparsecheckout true，打开sparse checkout功能。 第五第六条命令echo "path1/" &gt;&gt; .git/info/sparse-checkout，添加2个目录到checkout的列表。路径是版本库下的相对路径，也可以用文本编辑器编辑这个文件。 第七条命令git pull origin master，拉取远程的 master 分支，也可以拉其他分支。

