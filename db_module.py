import sqlite3

def create_database():
    connection = sqlite3.connect('mft.db')
    connection.close()

def save(title,teacher,unit):
    connection = sqlite3.connect('mft.db')
    connection.cursor().execute("insert into lessons (title, teacher, unit) values(?,?,?,?)", [title,teacher,unit])
    connection.commit()
    connection.close()


def delete(id):
    connection = sqlite3.connect('mft.db')
    connection.cursor().execute("delete from lessons where id = ?", [id])
    connection.commit()
    connection.close()

def update(id,title,teacher,unit):
    connection = sqlite3.connect('mft.db')
    connection.cursor().execute("update lessons set title=?, teacher=?, unit=? where id=?", [id,title,teacher,unit])
    connection.commit()
    connection.close()
