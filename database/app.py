from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/createdb')
def create_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.close()
    return 'Database created successfully'


@app.route('/insertdata')
def insert_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
                   ('John', 'john@example.com'))
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
                   ('Jane', 'jane@example.com'))
    conn.commit()
    conn.close()
    return 'Data inserted successfully'


# @app.route('/showdata')
# def show_data():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users")
#     data = cursor.fetchall()
#     conn.close()
#     return str(data)
@app.route('/showdata')
def show_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return render_template('showdata.html', data=data)


if __name__ == '__main__':
    app.run()
