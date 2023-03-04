import mysql.connector

#Create a connection to the DATABASE
conn = mysql.connector.connect(
    host='localhost',
    user='root', 
    password='root',
    database='tutorial'
)

#Create a cursor object
cursor = conn.cursor()

#Create a new DATABASE named tutorial
cursor.execute("CREATE DATABASE IF NOT EXISTS tutorial")
#Create a new TABLE named person
cursor.execute("CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY, name VARCHAR(64))")
#Create a new TABLE named thing
cursor.execute("CREATE TABLE IF NOT EXISTS thing (id INT PRIMARY KEY, name VARCHAR(64))")
#Create a new TABLE named owns
cursor.execute("""
CREATE TABLE IF NOT EXISTS owns (
person INT,
thing INT,
FOREIGN KEY (person) REFERENCES person(id),
FOREIGN KEY (thing) REFERENCES thing(id)
);
""")

cursor.execute("SHOW TABLES")

#Iterate throug cursor then print all the table
for table in cursor:
    print(table)

#Insert Element into the person table
cursor.execute("""
INSERT INTO person (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Marc');
""")

#Insert Element into the thing table
cursor.execute("""
INSERT INTO thing (id, name) VALUES
(1, 'Apple'),
(2, 'Box'),
(3, 'Computer');
""")

#Insert Element into the owns table
cursor.execute("""
INSERT INTO owns (person, thing) VALUES
(2, 1),
(2, 3),
(1, 2);
""")

class Person:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    def print_info(self):
        print(self.id, self.name)

    def from_result(self, row):
        self.id = row[0]
        self.name = row[1]

    def to_database(self, cursor):
        #Do not do it like that, it's the best way to get an SQL injection !
        cursor.execute(f"INSERT INTO person (id, name) VALUES ({self.id}, '{self.name}')")

#Retrieve data from person table
cursor.execute("SELECT * FROM person")

result = cursor.fetchall()

#create a new instance of the class PERSON and pass arguments
p1 = Person(8, "Mike")

p1.to_database(cursor)

for row in result:
    p = Person()
    p.from_result(row)
    p.print_info()

#Update the database
conn.commit()












