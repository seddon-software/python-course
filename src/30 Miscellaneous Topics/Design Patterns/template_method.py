############################################################
#
#    Template Method
#
############################################################


class Employee:
    # this method is partially defined in the base class
    # ... and partially defined in the derived class
    def ChangeDepartment(self):
        self.SetDepartment()    # defined in base class
        self.SetSalary()        # defined in derived class
        self.Register()         # overridden in some derived classes 

    def SetDepartment(self):
        print("SetDepartment for all employees")

    def Register(self):
        print("Register for all employees")


class FullTime(Employee):
    def SetSalary(self): 
        print("SetSalary for Full Time employees")


class PartTime(Employee):
    def SetSalary(self): 
        print("SetSalary for Part Time employees")
    
    def Register(self):
        print("Register for Part Time employees")

############################################################

john = FullTime()
sue = PartTime()
john.ChangeDepartment()
print()
sue.ChangeDepartment()
