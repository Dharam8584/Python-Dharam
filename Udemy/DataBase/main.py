import _sqlite3
import csv
#creating Data base with joins 
connection = _sqlite3.connect('myEmployees.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees
               (Emp_id INT , Emp_name TEXT, position TEXT , Salary INT , DEPT_ID INT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Department
               (DEPT_ID INT , Department_name)''')
# country = input('Please enter the Country Name ; ')
# city= input('PLease enter the City Name ')
# population = input('PLease enter the population name')

# connection = _sqlite3.connect("hr.db")
# cursor = connection.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS Employees
#                 (Emp_iD INT, NAME TEXT, Position TEXT)''')
# employess = [(5,'Dharamkar Nitesh', 'Business'),
#             (6,'Dharamkar Dinesh', 'Cricket player'),
#             (7,'Dandotikar Apurva', 'House wife')]

# #cursor.execute('''INSERT INTO Employees (Name,POSITION) VALUES(?,?)''',(name, position))
# cursor.executemany('''INSERT INTO Employees VALUES (?,?,?)''', employess)
# connection.commit()
# connection.close()
# connection = _sqlite3.connect('Data.db')
# cursor = connection.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS Population 
#                 (City TEXT,Country TEXT,Population INT )''')

# file = open('population_data.csv')
# city_data = csv.reader(file)
# city_data.__next__()
# #cursor.executemany(''' INSERT INTO Population VALUES (?, ? , ?)''',city_data)
# results = cursor.execute('''SELECT CITY, Country FROM Population WHERE COUNTRY = "India"''')
# for row in results:
#      print(row)
#results = cursor.execute('''INSERT INTO Population (Country, CITY, Population) VALUES (?,?,?)''',(country,city,population))

connection.commit()
connection.close