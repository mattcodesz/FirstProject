# main file to hold all the code relevant to making an employee

# This is the superclass Person; it is used to make the base of everything.
# This program can become more than just employee; can be anything related to person
class Person():
    # sets up values of object
    def __init__(self, firstName, lastName, SSN):
        self.firstName = firstName
        self.lastName = lastName
        self.SSN = SSN

    # custom string method to print out object details
    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.SSN

    # this function returns the name of the employee
    def getName(self):
        return self.firstName + ' ' + self.lastName

    # returns the SSN
    def getSSN(self):
        return self.SSN

    # function sets the name; either first or last
    def setName(self, first=None, last=None):
        if first != None:
            if last != None:
                # if both fields are not empty then both names are changed
                self.firstName = first
                self.lastName = last
                return
            # if last name is empty then only the first name is changed
            self.firstName = first
        # for use if first name is empty
        elif last != None:
            self.lastName = last

    # changes the SSN
    def setSSN(self, SSN):
        self.SSN = SSN

# Employee class that houses functions related to the employee
class Employee(Person):
    # initializes the list for employees
    employeeList = []

    def __init__(self, fname, lname, ssn, employeeID, company, position, salary):
        # Super constructor to utilize the parent class
        super().__init__(fname, lname, ssn)
        self.employeeID = employeeID
        self.company = company
        self.position = position
        self.salary = salary
        self.employeeList.append(self)

    # prints the object with relevant information; rounds salary to 2 decimal places
    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ' + self.employeeID + ' ' + self.company + ' ' + self.position + ' ' + str(
            round(self.salary, 2))

    # simple getters
    def getEmployeeID(self):
        return self.employeeID

    def getCompany(self):
        return self.company

    def getPosition(self):
        return self.position

    def getSalary(self):
        return self.salary

    # simple setters
    def setEmployeeID(self, new_id):
        self.employeeID = new_id

    def setCompany(self, company):
        self.company = company

    def setPosition(self, position):
        self.position = position

    def setSalary(self, salary):
        self.salary = salary

    #function to calculate the raise for an employee and apply it
    def Raise(self, percentage):
        currSal = self.getSalary()
        # gives the amount the raise is and adds it to current salary
        amtRaise = (percentage * .01) * currSal
        newSal = currSal + amtRaise
        self.setSalary(newSal)

    # same as the raise function except we subtract the amount from the salary and apply it
    def Cut(self, percentage):
        currSal = self.getSalary()
        amtCut = (percentage * .01) * currSal
        newSal = currSal - amtCut
        self.setSalary(newSal)

    # gets the amount of money made in a year
    def perYear(self):
        # get the salary
        currSal = self.getSalary()
        # multiply salary by 40 hour week (assumes 40 hour work week) then multiply that by 52 (weeks in year)
        year = (currSal * 40) * 52
        return year

# need to have one employee initialized here so the list works
employee = Employee('Tommy', 'Jackson', '278118369', '215', 'Hilton', 'Greeter', 14.25)

#prints the list of employees
def printList():
    for i in employee.employeeList:
        # can add different things here to specify certain employees to return
        # such as by company, etc.
        print(i)
