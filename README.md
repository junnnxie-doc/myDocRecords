# myDocRecords

进入本地存放代码的文件夹，git初始化，把github的ssh地址添加上，如果有多分支，进入main分支

要上传必须和远程仓库保持数据内容同步，第一次上传时，要先把远程仓库的数据git下来pull，再把本地数据加进去上传

上传通过add，commit和push操作


git init  

git remote add origin git@github.com:junnnxie-doc/myDocRecords.git

git init -b main

git pull origin main --allow-unrelated-histories

git add xxx.py

git commit -m 'xxx' 

git push -u origin main


如果要删除main以外的分支，git branch -a 查看当前所有分支，如删除master分支，git push origin --delete master
