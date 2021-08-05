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
    employeeList = []

    def __init__(self, fname, lname, ssn, employeeID, company, position, salary):
        super().__init__(fname, lname, ssn)
        self.employeeID = employeeID
        self.company = company
        self.position = position
        self.salary = salary
        self.employeeList.append(self)

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ' + self.employeeID + ' ' + self.company + ' ' + self.position + ' ' + str(
            round(self.salary, 2))

    def getEmployeeID(self):
        return self.employeeID

    def getCompany(self):
        return self.company

    def getPosition(self):
        return self.position

    def getSalary(self):
        return self.salary

    def setEmployeeID(self, new_id):
        self.employeeID = new_id

    def setCompany(self, company):
        self.company = company

    def setPosition(self, position):
        self.position = position

    def setSalary(self, salary):
        self.salary = salary

    def Raise(self, percentage):
        currSal = self.getSalary()
        amtRaise = (percentage * .01) * currSal
        newSal = currSal + amtRaise
        self.setSalary(newSal)

    def Cut(self, percentage):
        currSal = self.getSalary()
        amtCut = (percentage * .01) * currSal
        newSal = currSal - amtCut
        self.setSalary(newSal)


employee = Employee('Tommy', 'Jackson', '278118369', '215', 'Hilton', 'Greeter', 14.25)


def printList():
    for i in employee.employeeList:
        print(i)
