class Salary():
    def __init__(self,pay,bonus) -> None:
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12)+self.bonus

class Employee():
    def __init__(self,name,age,sal) -> None:
        self.name = name
        self.age = age
        self.agg_salary = sal

    def total_sal(self):
        return self.agg_salary.annual_salary()

sal1=Salary(1000000,200000)
sal2=Salary(4000000,0)
emp1=Employee('Ken',27,sal2)
print(f'total salary {emp1.name} adalah {emp1.total_sal()}')