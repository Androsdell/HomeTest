class Person:
    count = 0
    staff = 0
    all_salary = 0
    all_sal_staff = 0
    staff_assistants = []
    sal_staff = []
    
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
        self.__class__.count += 1
        self.__class__.all_salary += self.salary
        if self.status != "Detailee":
            self.__class__.staff += 1
        if self.status != "Detailee":
            self.__class__.all_sal_staff +=self.salary
        if self.position_title == "STAFF ASSISTANT":
            self.__class__.staff_assistants.append(self.name)
        if self.position_title == "STAFF ASSISTANT":
            self.__class__.sal_staff.append(self.salary)

    
    def __del__(self):
        self.__class__.count -= 1
        self.__class__.all_salary -= self.salary
        if self.status != "Detailee":
            self.__class__.staff -= 1
        if self.position_title == "STAFF ASSISTANT":
            self.__class__.staff_assistants.remove(self.name)
        
            
    def __repr__(self):
        return self.name
    
    @classmethod
    def report(self):
        print(f'''Всего {self.count} сотрудников
общая зарплата {self.all_salary}
средняя зарплата {float(self.all_salary / self.count):.2f}
средняя зарплата штатных сотрудников {float(self.all_sal_staff/ self.staff):.2f}''')
    
    @classmethod
    def assistants_report(self):
        for i,j in zip(self.staff_assistants,self.sal_staff):
            print(f'''assistant: {i}      / salary: {j}''' )

        
        
class WH:
    
    def __init__(self, name_file):
        self.sotr = []
        self.get_sotr(name_file)
        
    def get_sotr(self, name_file):
        f = open(name_file, 'r')
        t = f.readlines()
        f.close()
        for s in t[1:]:
            sp = s.strip().split(';')
            k = sp[2]
            salary = float(k.strip().replace('$','').replace(',',''))
            p = Person(sp[0], sp[1], salary, sp[3], sp[4])
            self.sotr.append(p)
            
    def recount(self):
        su = 0
        for s in self.sotr:
            su += s.salary
        Person.all_salary = su
        
    def summa(self):
        su = 0
        for s in self.sotr:
            su += s.salary
        return su/len(self.sotr)
        
    def top10(self):
        def sal(i):
            return i.salary
        top = self.sotr.copy()
        top2 = sorted(top, key=sal, reverse = True)
        return top2[:10]
        
    def detailees(self):
        return [i for i in self.sotr if i.status == 'Detailee' ]
        
    def staff(self):
        return len([i for i in self.sotr if i.position_title == 'STAFF ASSISTANT' ])
        
    def rep(self):
        for i in self.sotr:
            print(i)
            
    def count_sotr(self):
        print(f'Всего {Person.count} сотрудников, из них {Person.staff} на постоянной основе общий заработок {Person.all_salary}')
    
    @staticmethod
    def sum_salary():
        print(f'Сумма зарплат сотрудников: {Person.all_salary}')
    
    @staticmethod
    def avg_salary():
        print(f'Средняя зарплата сотрудников: {float(Person.all_salary/ Person.count):.2f}')

wh = WH('white_house_2017_salaries_com.csv')
per = Person


per.report()
print()
per.assistants_report()
print()
wh.sum_salary()
print()
wh.avg_salary()


