# 0x0F-python-object_relational_mapping
# Background Context
In this project, there would linking between two amazing worlds: Databases and Python!

In the first part, `MySQLdb` module would be used to connect a MySQL dabatabe
and execute SQL queries.

In the second part, `SQLAlchemy` would be used, which is an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is
to abstract the storage to the usage. With an ORM, the biggest concern would be
"What can I do with my objects" and not "How this object is stored?", "Where?" or
"When?". Any SQL queries won't be written but only Python code.

More so, The code won't be "storage type" dependent. The storage would be able to
be changed easily without re-writing the entire project.

Without ORM:

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

With an ORM:

```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

But, the biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always.

# More Info
## Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```python
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```
## Install MySQLdb module version 2.2.x
For installing MySQLdb, you need to have MySQL installed: [How to install MySQL 8.0 in Ubuntu 20.04](../0x0D-SQL_introduction/README.md)
```python
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo apt-get install pkg-config
$ pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 2, 0, 'final', 0)
```

## Install SQLAlchemy module version 2.0.x
```python
$ pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'2.0.23'
```
Also, you can have this warning message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")
  cursor.execute(statement, parameters)
  ```
  You can ignore it.
