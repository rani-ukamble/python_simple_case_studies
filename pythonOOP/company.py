from emp import Employee
# filename and classname

class Company:
    def __init__(self):
        self.employee = []

    def add_employee(self, new_emp):
        self.employee.append(new_emp)

    def display_emp(self):
        for i in self.employee:
            print(i.fname, i.lname)
            print("****************")

    def pay_check_amt(self):
        for i in self.employee:
            print("paycheck for ", i.fname, i.lname) 
            print(f"amount , ${i.checkSalary():,.2f}")       

def main():
    mycompany = Company()

    emp1 = Employee('Rani', 'Kamble', 9900000)

    mycompany.add_employee(emp1)

    emp2 = Employee('Ram', 'Kamble', 90000)
    
    mycompany.add_employee(emp2)

    mycompany.display_emp()

    mycompany.pay_check_amt()




if __name__ == '__main__':
    main()