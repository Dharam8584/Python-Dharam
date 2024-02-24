import _sqlite3

#name = input('Please enter the name ; ')
#position= input('PLease enter the position')

connection = _sqlite3.connect("hr.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees
                (Emp_iD INT, NAME TEXT, Position TEXT)''')
employess = [(5,'Dharamkar Nitesh', 'Business'),
            (6,'Dharamkar Dinesh', 'Cricket player'),
            (7,'Dandotikar Apurva', 'House wife')]

#cursor.execute('''INSERT INTO Employees (Name,POSITION) VALUES(?,?)''',(name, position))
cursor.executemany('''INSERT INTO Employees VALUES (?,?,?)''', employess)
connection.commit()
connection.close()