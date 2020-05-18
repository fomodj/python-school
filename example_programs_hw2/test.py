# '''
# 姓名：李润泽
# 学号：201701510045
# 程序：文件加密/解密程序
# 目的：复习Python文件的使用
# '''
#
# import os
# from os.path import exists
#
# # 读取加密所用的序列
# code = open('字符串.txt','r')
# sequence = code.readline()
#
# # 读取需要进行加密的信息
# def getinfo_encryption():
#     global profileName
#     profileName = input("请输入需要加密的文件名(无须后缀名)：")
#     fileName = profileName +'.txt'
#     if not exists(fileName):
#         print("该文件", fileName, "不存在！")
#         print('以下是本目录所有txt的文件：\n')
#         path = os.getcwd()
#         files = os.listdir(path)
#         for file in files:
#             if file.endswith('.txt'):
#                 print(file)
#     else:
#         file = open(fileName,'r')
#         global data
#         data = ''
#         line = file.readline()
#         while line:
#             data += line
#             line = file.readline()
#         return data
#
# # 读取需要进行解密的信息
# def getinfo_decryption():
#     global profileName1
#     profileName1 = input("请输入需要解密的文件名(无须后缀名)：")
#     fileName = profileName1 +'.zzz'
#     if not exists(fileName):
#         print("该文件", fileName, "不存在！")
#         print('以下是本目录所有zzz的文件：\n')
#         path = os.getcwd()
#         files = os.listdir(path)
#         for file in files:
#             if file.endswith('.zzz'):
#                 print(file)
#     else:
#         file = open(fileName,'r')
#         global data1
#         data1 = ''
#         line = file.readline()
#         while line:
#             data1 += line
#             line = file.readline()
#         return data1
#
# # 定义加密函数
# def encryption(data):
#     while True:
#         k = eval(input("请输入用于加密的正整数密钥："))
#         if isinstance(k, int) and k > 0:
#             print('已确认密钥为',k)
#             break
#         else:
#             print('输入错误')
#     str = data
#     str1 = ''
#     # 对第一个字母进行加密，密钥为K
#     str1 += sequence[(sequence.find(str[0])+k)%78]
#     for i in range(1,len(str)):
#         # 不在序列中的消息字符直接复制进加密信息
#         if str[i] not in sequence:
#             str1 += str[i]
#         else:
#             if str[i-1] not in sequence:
#             # 倘若需要加密信息的前一个是无需加密的，使用前一个有效移位量
#                 str1 += sequence[(sequence.find(str[i]) + sequence.find(str[i - 4])) % 78]
#             else:
#             # 需要加密的信息所使用的移位量
#                 str1 += sequence[(sequence.find(str[i]) + sequence.find(str[i - 1])) % 78]
#     print("加密内容为：")
#     print(str1,end='\n')
#     if not exists(profileName+'.zzz'):
#         with open(profileName+'.zzz','w') as fw:
#             fw.write(str1)
#     else:
#         order=input("同名文件已存在，是否删除？(y/n)\n")
#         if order == 'y':
#             os.remove(profileName+'.zzz')
#             with open(profileName + '.zzz', 'w') as fw:
#                 fw.write(str1)
#         else:
#             newname = input("请输入新的文件名(无须后缀)：")
#             with open(newname + '.zzz', 'w') as fw:
#                 fw.write(str1)
#     print("数据加密完成！退出请按“q”键！")
#
#
#
# # 定义解密函数
# def decryption(data1):
#     while True:
#         k = eval(input("请输入用于解密的正整数密钥："))
#         if isinstance(k, int) and k > 0:
#             print('已确认密钥为',k)
#             break
#         else:
#             print('输入错误')
#     str = data1
#     str1 = ''
#     # 对第一个字母进行解密，密钥为K
#     str1 += sequence[(sequence.find(str[0])-k)%78]
#     for i in range(1, len(str)):
#         # 不在序列中的消息字符直接复制进解密信息
#         if str[i] not in sequence:
#             str1 += str[i]
#         else:
#             if str[i - 1] not in sequence:
#                 # 倘若需要解密信息的前一个是无需解密的，使用前一个有效移位量
#                 str1 += sequence[(sequence.find(str[i]) - sequence.find(str1[i - 4])) % 78]
#             else:
#                 # 需要解密的信息所使用的移位量
#                 str1 += sequence[(sequence.find(str[i]) - sequence.find(str1[i - 1])) % 78]
#     print("解密内容为：")
#     print(str1, end='\n')
#     if not exists(profileName1 + '.txt'):
#         with open(profileName1 + '.txt', 'w') as fw:
#             fw.write(str1)
#     else:
#         order = input("同名文件已存在，是否删除原文件？(y/n)\n")
#         if order == 'y':
#             os.remove(profileName1 + '.txt')
#             with open(profileName1 + '.txt', 'w') as fw:
#                 fw.write(str1)
#         else:
#             newname = input("请输入新的文件名(无须后缀)：")
#             with open(newname + '.txt', 'w') as fw:
#                 fw.write(str1)
#     print("数据加密完成！退出请按“q”键！")
#
# # 菜单切换
# def run():
#     while True:
#         order = input("请输入指令：")
#         if order not in ['e','d','q']:
#             print("指令输错误，请重新输入！")
#         else:
#             if order == 'e':
#                 while getinfo_encryption():
#                     encryption(data)
#                     break
#             elif order == 'd':
#                 while getinfo_decryption():
#                     decryption(data1)
#                     break
#             elif order == 'q':
#                 print("程序结束，谢谢使用！")
#                 break
#
# # 主函数
# def main():
#     info = '''
# ****加密/解密程序菜单***
#       1.加密请按“e”
#       2.解密请按“d”
#       3.退出请按“q”
# ***********************
#     '''
#     print(info)
#     run()
#
# if __name__ == "__main__":
#     main()
def key():
    while True:
        k = input("请输入正整数密钥：")
        if k.isnumeric() == True and int(k) > 0:
            print('已确认密钥为', k)
            break
        else:
            print('输入错误')
    return k
print(type(int(key())))