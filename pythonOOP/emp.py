class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def checkSalary(self):
        return self.salary/52
    
    
    
