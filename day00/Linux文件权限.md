#Linux文件权限
ls -l 查看文件权限
#####修改文件权限
sudo chmod -
语法为：chmod abc file
其中a,b,c各为一个数字，分别表示User、Group、及Other的权限

>r=4，w=2，x=1 
>若要rwx属性则4+2+1=7； 
>若要rw-属性则4+2=6； 
>若要r-x属性则4+1=7。 

示例  `chmod a=rwx file` 等同于 `chmod 777 file`

#####修改文件拥有者
__chown__ user:group file 来改变拥有者并且赋予相应的权限