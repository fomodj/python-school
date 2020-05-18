from overload.rational import Rational

r1 = Rational(5,6)
r2 = Rational(15,7)

print(r1)
print(r2)
print(r1+r2)
print(r1-r2)
print(r1*r2)
print(r1/r2)
print(Rational.gcd(r1,r2))                       
print("r1==r2?",r1==r2)
print("r1<r2?",r1<r2)            