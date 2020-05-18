# 读取初始数据
def recover_info(dict):
    f = open("data.txt", 'r',encoding='utf-8')
    list1 = []
    line = f.readline()
    while line != "":
        line0 = line.rstrip()
        line1 = line0.split()
        list1.append(line1)
        line = f.readline()
    for i in list1:
        dict[i[0]] = i[1]


# 添加联系人函数
def add(dict):
    name = input("请输入姓名：")
    flag = False  # 判断是否已经存储，默认未存储
    for i in range(len(dict)):
        if name in dict:
            print("该联系人已存在，请重新输入！")
            flag = True
            break
    if not flag:
        phone = input("请输入手机号码：")
        dict[name] = phone
        print("输入完成")

# 删除联系人函数
def delete(dict):
    name = input("请输入需要删除的联系人：")
    flag = False # 判断是否已经存在，默认不存在
    if name in dict:
        del dict[name]
        flag = True
        print("已删除成功")
    if not flag:
        print("没有该联系人记录！")

# 修改联系人函数
def update(dict):
    name = input("请输入需要修改的联系人：")
    flag = False  # 判断是否已经存在，默认不存在
    if name in dict:
        phone = input("请输入需要修改的电话号码：")
        dict[name] = phone
        flag = True
        print("修改完成")
    if not flag:
        print("没有该联系人记录！")

# 查询联系人函数
def search(dict):
    name = input("请输入需要查询的联系人：")
    flag = False  # 判断是否已经存在，默认不存在
    if name in dict:
        print("您所查询的联系人的电话号码是：%s"%dict[name])
        flag = True
    if not flag:
        print("没有该联系人记录！")

# 显示所有联系人函数
def showall(dict):
    print("*********************")
    for key, value in dict.items():
        print('联系人信息：'+ key + ' ' + value)
    print("*********************")

# 保存数据
def savedata(dict):
    f = open("data.txt", 'w',encoding='utf-8')
    for k, v in dict.items():  # 遍历字典中的键值
        s2 = str(v)  # 把字典的值转换成字符型
        f.write(k + " "+ s2 + '\n')
    f.close()
    print("保存文件成功")

# 菜单切换
def run(dict):
    while True:
        order = input("请输入指令：")
        if order not in ['0','1','2','3','4','5','6']:
            print("指令输错误，请重新输入！")
        else:
            if order == '1':
                add(dict)
            elif order == '2':
                delete(dict)
            elif order == '3':
                update(dict)
            elif order == '4':
                search(dict)
            elif order == '5':
                showall(dict)
            elif order == '6':
                savedata(dict)
            elif order == '0':
                print("程序结束，谢谢使用！")
                break

# 主函数
def main():
    # 创建空字典
    dict = {}
    info = '''
******通讯录命令菜单******
1.添加联系人   2.删除联系人
3.修改联系人   4.查询联系人
5.所有联系人   6.保存数据
     输入0时，结束程序
*************************'''
    print(info)
    recover_info(dict)
    run(dict)


if __name__=="__main__":
    main()



