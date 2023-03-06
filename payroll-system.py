class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    
class SalaryEmployee(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def calculate_payroll(self):
        return self.salary

class CommissionEmployee(SalaryEmployee):
    def __init__(self, name, id, salary, commission):
        super().__init__(name, id, salary)
        self.salary = salary
        self.commission = commission

    def calculate_payroll(self):
        return self.salary + self.commission


class HourlyEmployee(Employee):
    def __init__(self, name, id, rate, hours_worked):
        super().__init__(name, id)
        self.rate = rate
        self.hours_worked = hours_worked

    def calculate_payroll(self):
        return self.rate * self.hours_worked


class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print(f"Payroll for: {employee.name}")
            print(f"Total amount: Ksh.{employee.calculate_payroll()}")
            print("")

employees = [
    SalaryEmployee("Lucas Mambo", 12345, 52000),
    CommissionEmployee("Simon Brian", 67890, 43000, 4500),
    HourlyEmployee("Kelvin David", 112233, 150, 160),
]

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)
