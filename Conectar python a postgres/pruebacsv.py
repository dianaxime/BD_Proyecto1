import csv

with open(r'employee_file.csv', mode='a+', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #employee_writer = csv.writer(employee_file)
    employee_writer.writerow(['Camila', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])