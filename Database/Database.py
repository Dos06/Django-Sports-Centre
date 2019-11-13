import pypyodbc
import sqlite3


# function to create a DB
def sqlite3_create_db():
    # create an empty Database
    con = sqlite3.connect(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3')

    # create a table in DB
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users('
                'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                'Name TEXT NOT NULL,'
                'Surname TEXT NOT NULL,'
                'Login TEXT NOT NULL UNIQUE,'
                'Password TEXT NOT NULL,'
                'Gender TEXT,'
                'Age INTEGER,'
                'Activity TEXT NOT NULL)')

    # fill in DB
    cur.execute('INSERT INTO users (Name, Surname, Login, Password, Gender, Age, Activity) '
                'VALUES("Dosbol", "Bakhtiyar", "dosbol", "dospass", "Male", 19, "crossfit")')

    person = ["Aldiyar", "Gabitov", "aldiyar", "aldipass", "Male", 18, "box"]
    cur.execute('INSERT INTO users (Name, Surname, Login, Password, Gender, Age, Activity) '
                'VALUES(?, ?, ?, ?, ?, ?, ?)', person)

    some_persons = []
    person1 = ["Asiin", "Satymbekov", "asiin", "asiinpass", "Male", 18, "gym"]
    person2 = ["Bekezhan", "Issabek", "bekezhan", "bekapass", "Male", 18, "gym"]
    some_persons.append(person1)
    some_persons.append(person2)
    for pers in some_persons:
        cur.execute('INSERT INTO users (Name, Surname, Login, Password, Gender, Age, Activity) '
                    'VALUES(?, ?, ?, ?, ?, ?, ?)', pers)

    con.commit()  # save table
    cur.close()
    con.close()


def print_data_in_table(columns_names, data):
    print(columns_names)
    for line in data:
        print(line)
    print('Number of records in a DB is:', len(data))


# function to read a DB
def sqlite3_read_db(database, table, column_name=None):
    # connect the DB
    con = sqlite3.connect(database)
    # create a cursor object
    cur = con.cursor()
    query_columns = 'pragma table_info(' + table + ')'
    cur.execute(query_columns)
    columns_description = cur.fetchall()
    columns_names = []
    for column in columns_description:
        columns_names.append(column[1])

    if column_name is None:
        query = 'SELECT * FROM ' + table
        cur.execute(query)
        data = cur.fetchall()
    else:
        query = 'SELECT ' + column_name + ' FROM ' + table
        cur.execute(query)
        data = cur.fetchall()
        new_data = []
        for element in data:
            new_data.append(element[0])
        data = new_data
        del new_data
    print_data_in_table(columns_names, data)

    # # make a query to a DB (sort by Name)
    # cur.execute('SELECT ID, Name, Surname, Login, Password, Gender, Age, Activity FROM users ORDER BY Name')
    # data = cur.fetchall()

    cur.close()
    con.close()
    return data


# function to delete a table from DB
def sqlite3_delete_table(database, table):
    # connect the DB
    con = sqlite3.connect(database)
    # create a cursor object
    cur = con.cursor()

    query = 'DROP TABLE IF EXISTS ' + table
    cur.execute(query)

    con.commit()  # save table
    cur.close()
    con.close()


# function to delete a record from a table in a DB
def sqlite3_delete_record(database, table, column, row):
    # connect the DB
    con = sqlite3.connect(database)
    # create a cursor object
    cur = con.cursor()
    # create a query to delete a record 'row' in a 'column'
    query = 'DELETE FROM ' + table + ' WHERE ' + column + " = '" + row + "'"
    cur.execute(query)

    con.commit()  # save table
    cur.close()
    con.close()


# function to update a record in a table in a DB
def sqlite3_update_record(database, table, column, row, parameter_column, parameter_value):
    # connect the DB
    con = sqlite3.connect(database)
    # create a cursor object
    cur = con.cursor()
    # create a query to update a record 'row' in a 'column'
    query = 'UPDATE ' + table + ' SET ' + parameter_column + '=' + '"' + str(parameter_value) + '"' + \
            ' WHERE ' + column + " = '" + str(row) + "'"
    cur.execute(query)

    con.commit()  # save table
    cur.close()
    con.close()


# a function to add a new member to DB (table 'Members')
def sqlite3_add_member_to_db(name, surname, login, password, gender, age, activity):
    con = sqlite3.connect(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3')
    cur = con.cursor()
    person = [name, surname, login, password, gender, age, activity]
    cur.execute('INSERT INTO users (Name, Surname, Login, Password, Gender, Age, Activity) '
                'VALUES(?, ?, ?, ?, ?, ?, ?)', person)
    con.commit()
    cur.close()
    con.close()


# function to create a table for 1 activity in particular
def sqlite3_create_table(activity):
    con = sqlite3.connect(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3')

    # create a table in DB
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ' + activity + '('
                'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
                'Name TEXT NOT NULL,'
                'Surname TEXT NOT NULL,'
                'Gender TEXT,'
                'Age INTEGER)')

    con.commit()  # save table
    cur.close()
    con.close()


# a function to add a new member to DB (table 'Members')
def sqlite3_add_member_to_table(table, name, surname, gender, age):
    con = sqlite3.connect(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3')
    cur = con.cursor()
    person = [name, surname, gender, age]
    cur.execute('INSERT INTO ' + table + ' (Name, Surname, Gender, Age) '
                'VALUES(?, ?, ?, ?)', person)
    con.commit()
    cur.close()
    con.close()


def sqlite3_get_user(table, activity):
    con = sqlite3.connect(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3')
    cur = con.cursor()

    query = "SELECT Name, Surname, Gender, Age FROM " + table + " WHERE Activity = " + '"' + activity + '"'
    cur.execute(query)

    persons_activity = []
    for pers in persons_activity:
        sqlite3_add_member_to_table('"' + activity + '"', pers)

    con.commit()
    cur.close()
    con.close()


# sqlite3_create_db()
# sqlite3_delete_table(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3', 'users')
# sqlite3_update_record(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3',
#                       'users', 'Surname', 'McGregor', 'Password', 'conorpass')
# sqlite3_read_db(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3',
#                 'users')  # sqlite3_read_db(DB.sqlite3', 'users', 'Name')
# Name may be replaced by any column

# sqlite3_delete_record(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3', 'users', 'Login', 'bekezhan')

# sqlite3_add_member_to_db('Mariya', 'Sharapova', 'mariya', 'mariyapass', 'Female', 32, 'crossfit')
# sqlite3_add_member_to_db('Sabina', 'Altynbekova', 'sabina', 'sabinapass', 'Female', 23, 'volleyball')
# sqlite3_add_member_to_db('Gennady', 'Golovkin', 'gennady', 'gennadypass', 'Male', 37, 'box')
# sqlite3_add_member_to_db('Mike', 'Tyson', 'mike', 'mikepass', 'Male', 53, 'box')
# sqlite3_add_member_to_db('Hannah', 'Tapp', 'hannah', 'hannahpass', 'Female', 24, 'volleyball')
# sqlite3_add_member_to_db('Louisa', 'Lippmann', 'louisa', 'louisapass', 'Female', 25, 'volleyball')
# sqlite3_add_member_to_db('Oscar', 'Hartmann', 'oscar', 'oscarpass', 'Male', 37, 'crossfit')
# sqlite3_add_member_to_db('Igor', 'Ozernoy', 'igor', 'igorpass', 'Male', 46, 'gym')
# sqlite3_add_member_to_db('Fedor', 'Yemelyanenko', 'fedor', 'fedorpass', 'Male', 43, 'box')
#
# sqlite3_create_table('box')
# sqlite3_create_table('crossfit')
# sqlite3_create_table('gym')
# sqlite3_create_table('volleyball')

# sqlite3_get_user('users', 'crossfit')

# sqlite3_add_member_to_table('crossfit', 'Dosbol', 'Bakhtiyar', 'Male', 19)
# sqlite3_add_member_to_table('crossfit', 'Mariya', 'Sharapova', 'Female', 32)
# sqlite3_add_member_to_table('crossfit', 'Oscar', 'Hartmann', 'Male', 37)
# sqlite3_add_member_to_table('box', 'Aldiyar', 'Gabitov', 'Male', 18)
# sqlite3_add_member_to_table('box', 'Gennady', 'Golovkin', 'Male', 37)
# sqlite3_add_member_to_table('box', 'Mike', 'Tyson', 'Male', 53)
# sqlite3_add_member_to_table('box', 'Fedor', 'Yemelyanenko', 'Male', 43)
# sqlite3_add_member_to_table('gym', 'Asiin', 'Satymbekov', 'Male', 18)
# sqlite3_add_member_to_table('gym', 'Bekezhan', 'Issabek', 'Male', 18)
# sqlite3_add_member_to_table('gym', 'Igor', 'Ozernoy', 'Male', 46)
# sqlite3_add_member_to_table('volleyball', 'Sabina', 'Altynbekova', 'Female', 23)
# sqlite3_add_member_to_table('volleyball', 'Hannah', 'Tapp', 'Female', 24)
# sqlite3_add_member_to_table('volleyball', 'Louisa', 'Lippmann', 'Female', 25)


sqlite3_read_db(r'C:\Users\agaga\PycharmProjects\Django-Sports-Centre\DB.sqlite3', 'users')
