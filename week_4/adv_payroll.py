Here is the Python code for the advanced payroll system:

```python
class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        overtime_hours = max(0, self.hours_worked - 40)
        regular_hours = min(self.hours_worked, 40)
        total_pay = (regular_hours * self.hourly_rate) + (overtime_hours * 1.5 * self.hourly_rate)
        return total_pay

class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        total_pay = base_pay + self.bonus
        return total_pay

employee_name = input("Enter Employee Name: ")
employee_hours_worked = float(input("Enter Hours Worked: "))
employee_hourly_rate = float(input("Enter Hourly Rate: "))
manager_name = input("Enter Manager Name: ")
manager_hours_worked = float(input("Enter Hours Worked: "))
manager_hourly_rate = float(input("Enter Hourly Rate: "))
manager_bonus = float(input("Enter Bonus: "))

employee = Employee(employee_name, employee_hours_worked, employee_hourly_rate)
manager = Manager(manager_name, manager_hours_worked, manager_hourly_rate, manager_bonus)

print(f"Total Pay for {employee.name}: {employee.calculate_pay()}")
print(f"Total Pay for {manager.name}: {manager.calculate_pay()}")
```
