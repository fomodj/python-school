from overload.rational import Rational
def add(x,y):
    return x+y
if __name__=="__main__":
    print(add(1,2))
    print(add("hello","world"))
    print(add(Rational(2,3),Rational(4,5)))