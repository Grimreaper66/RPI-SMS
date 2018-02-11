import sqlite3

def connect():
    conn=sqlite3.connect('phonebook.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, number TEXT)')
    conn.commit()
    conn.close()

def add (name, number):
    conn=sqlite3.connect('phonebook.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO contacts VALUES(NULL,?,?)',(name,number))
    conn.commit()
    conn.close()

def update (id, name, number):
    conn=sqlite3.connect('phonebook.db')
    cur=conn.cursor()
    cur.execute('UPDATE contacts SET name=?, number=? WHERE id=?',(name,number,id))
    conn.commit()
    conn.close()

def delete (id):
    conn=sqlite3.connect('phonebook.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM contacts WHERE id=?',(id,))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('phonebook.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM contacts')
    rows=cur.fetchall()
    conn.close()
    print('  ID    NAME      NUMBER')
    for row in rows:
        id = str(row[-3])
        name = str(row[1])
        number = str(row[2])
        print('  ' + id + '     ' + name + '    ' + number)

def find (id='', name='', number=''):
    conn=sqlite3.connect('phonebook.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM contacts WHERE id=? OR name=? OR number=?',(id,name,number))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    print('  ID    NAME      NUMBER')
    for row in rows:
        id = str(row[-3])
        name = str(row[1])
        number = str(row[2])
        print('  ' + id + '     ' + name + '    ' + number)

def get_number (id='', name='', number=''):
    conn=sqlite3.connect('phonebook.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM contacts WHERE id=? OR name=? OR number=?',(id,name,number))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        number_str = str(row[2])
        return number_str

connect()
