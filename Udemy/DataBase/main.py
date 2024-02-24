import _sqlite3
import csv

#name = input('Please enter the name ; ')
#position= input('PLease enter the position')

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
connection = _sqlite3.connect('Data.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Population 
                (City TEXT,Country TEXT,Population INT )''')

# file = open('population_data.csv')
# city_data = csv.reader(file)
# city_data.__next__()
# #cursor.executemany(''' INSERT INTO Population VALUES (?, ? , ?)''',city_data)
results = cursor.execute('''SELECT CITY, Country FROM Population WHERE COUNTRY = "I%"''')
for row in results:
    print(row)

connection.commit()
connection.close