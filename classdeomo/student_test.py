from classdeomo.student import Student
import random
s = Student("Marry",5)
print(s)
s.setScore(1,100)
print(s)
for i in range(1,s.getNumber()):
    s.setScore(i+1,random.randint(1,100))
print(s)
print("High score:",s.getHighScore())
print("Average score:",s.getAverage())