import csv

monthly_sales = {}

with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['Month']
        sales = int(row['Sales'])
        monthly_sales[month] = sales

print(monthly_sales)
