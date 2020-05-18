# 读取初始数据
def recover_info(list):
    f = open("data.txt", 'r')
    line = f.readline()
    while line != "":
        line0 = line.rstrip()
        line1 = line0.split()
        list.append(line1)
        line = f.readline()

# 添加联系人函数
def add(list):
    name = input("请输入姓名：")
    flag = False # 判断是否已经存储，默认未存储
    for i in range(len(list)):
        if list[i][0] == name:
            print("该联系人已存在，请重新输入！")
            flag = True
            break
    if not flag:
        phone = input("请输入手机号码：")
        addlist = [name,phone]
        list.append(addlist)
        print("输入完成")

# 删除联系人函数
def delete(list):
    name = input("请输入需要删除的联系人：")
    flag = False # 判断是否已经存在，默认不存在
    for i in range(len(list)):
        if list[i][0] == name:
            del list[i]
            flag = True
            print("已删除成功")
            break
    if not flag:
        print("没有该联系人记录！")

# 修改联系人函数
def update(list):
    name = input("请输入需要修改的联系人：")
    flag = False  # 判断是否已经存在，默认不存在
    for i in range(len(list)):
        if list[i][0] == name:
            phone = input("请输入需要修改的电话号码：")
            list[i][1] = phone
            flag = True
            print("修改完成")
            break
    if not flag:
        print("没有该联系人记录！")

# 查询联系人函数
def search(list):
    name = input("请输入需要查询的联系人：")
    flag = False  # 判断是否已经存在，默认不存在
    for i in range(len(list)):
        if list[i][0] == name:
            print("您所查询的联系人的电话号码是：{}".format(list[i][1]))
            flag = True
            break
    if not flag:
        print("没有该联系人记录！")

# 显示所有联系人函数
def showall(list):
    print("*********************")
    for i in list:
        print("联系人信息：\t%s\t\t%s"%(i[0],i[1]))
    print("*********************")

# 保存数据
def savedata(list):
    f = open("data.txt", 'w')
    for i in range(len(list)):
        s = str(list[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        f.write(s)
    f.close()
    print("保存文件成功")

# 菜单切换
def run(list):
    while True:
        order = input("请输入指令：")
        if order not in ['0','1','2','3','4','5','6']:
            print("指令输错误，请重新输入！")
        else:
            if order == '1':
                add(list)
            elif order == '2':
                delete(list)
            elif order == '3':
                update(list)
            elif order == '4':
                search(list)
            elif order == '5':
                showall(list)
            elif order == '6':
                savedata(list)
            elif order == '0':
                print("程序结束，谢谢使用！")
                break

# 主函数
def main():
    # 创建空列表
    list = []
    info = '''
******通讯录命令菜单******
1.添加联系人   2.删除联系人
3.修改联系人   4.查询联系人
5.所有联系人   6.保存数据
     输入0时，结束程序
*************************'''
    print(info)
    recover_info(list)
    run(list)


if __name__=="__main__":
    main()



