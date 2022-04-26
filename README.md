# shiyanlou-study
All The Practice Code Will be Placed Here
Demo Try

首先找到要上传的目录:
git init 初始化一下
(如果不想要了,或者出错了,rm -rf .git)

git branch -m master  # # 重新取个分枝名

git add . # 文件添加到仓库

git status # # 查看状态

git commit -m ‘first commit’ # # 把文件提交到仓库

git remote add origin + github ssh地址 # # 关联远程仓库

git push -u origin matser
到这一步可能会出现各种奇怪的错误,解决办法:
1. git pull origin master  
    git push -u origin master

2. git push -u origin master -f  # # 强制push

3. 创建新分支
    git branch 分枝名
    git push -u origin 分枝名


本地文件修改以后更改github文件:
git status

git add -A

git commit -a -m "update" 

git push origin master -f

具体还是看什么错误吧,出现错误面向百度编程,总有一款解决办法,稀里糊涂他就好了~

