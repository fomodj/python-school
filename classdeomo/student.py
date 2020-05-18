'''
s = Student(name,number) #number分数的个数
s.getName()
s.getScore(i) #返回该学生第i项分数
s.getScore(i,score) #表示将该学生的第i项成绩重置为新的分数Score
s.getAverage() #获取学生的平均分
s.getHighScore() #返回学生的最高分
print(s) #可以输出学生信息
'''
class Student:
    def __init__(self,name,number):
        self.__name = name
        self.__scores = []
        for i in range(number):
            self.__scores.append(0)
    def getName(self):
        return self.__name
    def getNumber(self):
        return len(self.__scores)
    def getScore(self,i):
        return self.__scores[i-1]
    def setScore(self,i,score):
        self.__scores[i-1] = score
    def getAverage(self):
        return sum(self.__scores)/len(self.__scores)
    def getHighScore(self):
        return max(self.__scores)
    def __str__(self):
        return "Name:"+self.__name+"\nScores:"+\
            " ".join(map(str,self.__scores))
