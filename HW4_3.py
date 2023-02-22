'''
Develop a function (and test how it works) that reads a comma-separated file (CSV) of the given name
(parameter) and stores the triples of values for each department (number of employees in the
department, total salary of those employees, the average salary of the employees) in a dictionary
called Depts (global variable).
The rows in the file have the following structure:
Name of employee,Departement name,Salary
This is the function’s signature:
fill_dept_stats(file_name)
After that, develop another function, which uses the Depts list to search for data:
get_dept_stats(dept_name)
If the data for the given department is not found, the function has to return all three zeros.
Call the first function once and then the second function a few times (with different department
names) to test how they both work. 
A sample file Emp_salary.csv is provided. I suggest to add more rows to it for testing.
'''

''' A couple things to Note: This program does not account for misspelling Dept names
they will be considered different departments if spelled correctly, but it does account for 
Capitalization and Spacing Errors when reading in files. Program will only run when all
conditions are satisfied.'''

Depts = {}

def fill_dept_stats(file_name):
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if len(line) > 1:
                    empInfo = line.split(',')
                    if len(empInfo) == 3:
                        dept = empInfo[1].lower().strip()
                        if dept not in Depts.keys():
                            Depts[dept] = {}
                            Depts[dept]['EmpNo'] = 1
                            Depts[dept]['TotalSalary'] = float(empInfo[2])
                            Depts[dept]['AvgSalary'] = float(empInfo[2])
                        else:    
                            Depts[dept].update({'EmpNo' : Depts[dept]['EmpNo'] + 1})
                            Depts[dept].update({'TotalSalary' : Depts[dept]['TotalSalary'] + float(empInfo[2])}) 
                            Depts[dept].update({'AvgSalary': Depts[dept]['TotalSalary']/Depts[dept]['EmpNo']})
                    else:
                        print("Inputs are not in the format: Name of employee,Departement name,Salary")
                        return -1
    except FileNotFoundError as e:
        print("File Not Found!")
        return -1
    except ValueError as e:
        print("Value Error! Check File Inputs")
        return -1
    return

def get_dept_stats(dept):
    dept = dept.lower()
    if dept not in Depts.keys():
        return 0, 0, 0
    return Depts[dept]['EmpNo'], Depts[dept]['TotalSalary'], Depts[dept]['AvgSalary']


if fill_dept_stats("Emp_salary.csv") == -1:
    print("Try Again!")
else:
    dept = "R&D"
    emp_no, total_sal, avg_sal = get_dept_stats(dept)
    print("Department: %s, Employees No.: %d, Total Salary: %.2f, Average Salary: %.2f" %(dept, emp_no, total_sal, avg_sal))
    dept = "Accounting"
    emp_no, total_sal, avg_sal = get_dept_stats(dept)
    print("Department: %s, Employees No.: %d, Total Salary: %.2f, Average Salary: %.2f" %(dept, emp_no, total_sal, avg_sal))
    dept = "CS"
    emp_no, total_sal, avg_sal = get_dept_stats(dept)
    print("Department: %s, Employees No.: %d, Total Salary: %.2f, Average Salary: %.2f" %(dept, emp_no, total_sal, avg_sal))