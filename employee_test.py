from employee import Employee
def main():
    # 数据
    people01 = Employee('Susan Meyers','47899','Accouting','Vice President')
    people02 = Employee('Mark John','39119','IT','Programmer')
    people03 = Employee('Joy Rogers','81774','Manufacturing','Engineer')

    print(people01.__str__()+'\n')
    print(people02.__str__()+'\n')
    print(people03.__str__())
main()