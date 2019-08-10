# 0x0F. Python - Object-Relational Mapping

## Resources
**Read or watch**:

Object-relational mappers
mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)
MySQLdb tutorial
SQLAlchemy tutorial
SQLAlchemy
mysqlclient/MySQLdb
Introduction to SQLAlchemy
Flask SQLAlchemy
10 common stumbling blocks for SQLAlchemy newbies
Python SQLAlchemy Cheatsheet

## Learning Objectives

### General

Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))?
How to connect to a MySQL database from a Python script?
How to SELECT rows in a MySQL table from a Python script?
How to INSERT rows in a MySQL table from a Python script?
What ORM means?
How to map a Python Class to a MySQL table?

## Tasks

**0. Get all states mandatory**
Write a script that lists all states from the database 

**1. Filter states mandatory**
Write a script that lists all states with a name starting with N (upper N) from the database 

**2. Filter states by user input mandatory**
Write a script that takes in an argument and displays all values in the states table 

**3. SQL Injection... mandatory**
Wait, do you remember the previous task? Did you test?

**4. Cities by states mandatory**
Write a script that lists all cities from the database

**5. All cities by state mandatory**
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database 

**6. First state model mandatory**
Write a python file that contains the class definition of a State and an instance Base = declarative_base():

**7. All states via SQLAlchemy mandatory**
Write a script that lists all State objects from the database 

**8. First state mandatory**
Write a script that prints the first State object from the database 

**9. Contains `a` mandatory**
Write a script that lists all State objects that contain the letter a from the database 

**10. Get a state mandatory**
Write a script that prints the State object with the name passed as argument from the database

**11. Add a new state mandatory**
Write a script that adds the State object “Louisiana” to the database

**12. Update a state mandatory**
Write a script that changes the name of a State object from the database 

**13. Delete states mandatory**
Write a script that deletes all State objects with a name containing the letter a from the database

**14. Cities in state mandatory**
Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

