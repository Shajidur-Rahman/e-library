# Data class
class Data:

    #making db

    import sqlite3
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    # creating database
    try:
        c.execute("""CREATE TABLE person(
        name TEXT,
        age INTEGER,
        email TEXT,
        pass TEXT,
        book TEXT
        )""")
    except:
        pass


    def add(self, name, age, email, password):
        self.c.execute("INSERT INTO person VALUES ('{}', '{}', '{}', '{}','N/A')".format(name, int(age), email, password))

    # show all users
    def users(self):
        self.c.execute('SELECT rowid, * FROM person')
        users = self.c.fetchall()
        print(users)

    # find users by id
    def find(self, id):
        self.c.execute('SELECT rowid, * FROM person')
        users = self.c.fetchall()
        try:
            if int(id) > 0:

                print(users[id - 1])
            else:
                print('Please enter the correct id ')

        except:
            print('Please enter the correct id')


    def delete(self, id):
        # get_password = self.c.execute("""SELECT *, rowid FROM person""")
        # get = get_password.fetchall()
        # get_password = get[int(id)][3]
        get_password = self.c.execute("""SELECT * FROM person WHERE rowid = {}""".format(id))
        get_password = get_password.fetchall()
        for i in get_password:
            pass
        # get_password = get_password[3]
        # print(get_password)
        try:
            password_get = input(f"Give me the password of {i[0]}: ")
            if password_get == i[3]:
                delete_db_user = self.c.execute("""DELETE FROM person WHERE rowid = {}""".format(id))
                self.conn.commit()
                print('DELETED SUCCESSFULLY')
            else:
                print('NOT DELETED')
            

        except Exception as error:
            print('something went worng', error)






if __name__ == '__main__':
    data = Data()

    # insert data
    # data.add('shajidur rahman',12, 'saad@gmail.com', 'saad')

    # show all users
    data.users()

    #finding
    # data.find(1)

    # deleteing account
    # data.delete(id = int(input('Give me your id number that you want to delete: ')))

    data.conn.commit()
    data.conn.close()