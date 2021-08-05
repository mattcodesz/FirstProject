class Person():
    def __init__(self, firstName, lastName, SSN):
        self.firstName = firstName
        self.lastName = lastName
        self.SSN = SSN

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.SSN

    def getName(self):
        return self.firstName + ' ' + self.lastName

    def getSSN(self):
        return self.SSN

    def setName(self, first=None, last=None):
        if first != None:
            if last != None:
                self.firstName = first
                self.lastName = last
                return
            self.firstName = first
        elif last != None:
            self.lastName = last

    def setSSN(self, SSN):
        self.SSN = SSN

class Employee(Person):
    def __init__(self, employeeID, company, position, salary):
        super().__init__('Matthew', 'Rickman', '279718811')
        self.employeeID = employeeID
        self.company = company
        self.position = position
        self.salary = salary

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ' + self.employeeID + ' ' + self.company + ' ' + self.position + ' ' + str(self.salary)

    def getEmployeeID(self):
        return self.employeeID

    def getCompany(self):
        return self.company

    def getPosition(self):
        return self.position

    def getSalary(self):
        return self.salary

    def setEmployeeID(self, id):
        self.id = id

    def setCompany(self, company):
        self.company = company

    def setPosition(self, position):
        self.position = position

    def setSalary(self, salary):
        self.salary = salary


person = Person("Matthew", "Rickman", "279719001")
employee = Employee('215', 'Hilton', 'Greeter', 14.25)
print(employee)
