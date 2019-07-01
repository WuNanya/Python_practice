#Author WuNan
import sys

input_number = 0  #已输入次数
f = open("user_info.txt","r")  #打开一个存放了用户信息的文件
f2 = open("user_lock.txt","r+") #存放了已经被锁定的用户的username
Flag = False    #用户名和密码是否输入正确的标志
_username = ''
_password = ''
for i in range(3):
    _username = input("请输入用户名->>")
    _password = input("请输入对应密码->>")
    for line in f2:
        if _username == line.strip():
            sys.exit("your user have been locked!")
    for line in f:    #遍历用户信息文件
        if _username == line.strip().split()[0] and _password == line.strip().split()[1]:
            #判断输入的用户名以及密码是否匹配
            print("you have login success!")
            Flag = True
            f.close()
            break
    if Flag == False:
        print("用户名或密码输入错误")
        continue
    if Flag == True:
        break
else:
    print("your user will be locked")
    f2.write(_username + "\n")   #输入三次后锁定
    f2.close()





