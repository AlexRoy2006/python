employee_information=[
    ("Raju","Finance",25000.00),
    ("Ramu", "Administration",50000.00),
    ("Rajesh","Hiring",100000.00),
    ("Raveendran","Public relation",150000.00)
]
threshhold=int(input("Enter a thresh hold:"))
for employee in employee_information:
    employee_name, department, monthly_salary = employee
    if monthly_salary>threshhold:
        print(employee_name)



