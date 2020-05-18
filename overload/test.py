# 求分子最大公约数
if a.__numeration > b.__numeration:
    smaller = b.__numeration
else:
    smaller = a.__numeration
for i in range(1, smaller + 1):
    if ((a.__numeration % i == 0) and (b.__numeration % i == 0)):
        new_nu = i
# 求分母最小公倍数
if a.__denominator > b.__denominator:
    greater = a.__denominator
else:
    greater = b.__denominator
while (True):
    if ((greater % a.__denominator == 0) and (greater % b.__denominator == 0)):
        new_de = greater
        break
    greater += 1
