# git

git remote rm origin 

git remote add origin ... 

git config master.remote origin 

git config master.merge refs/heads/master



### use different ssh key



```text
Host github.com:XuCongyu 
  User git 
  Hostname github.com 
  IdentityFile ~/.ssh/gitnyu
  
Host github.com:0is4car 
  User git 
  Hostname github.com 
  IdentityFile ~/.ssh/id_rsa
```



even though use key for 0is4car, but the weird thing is if use the email of XuCongyu as user.email the user commit is still 0is4car

