
import os
import sys
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="users_info"
)


class register1:
    def __init__(self):
        self.parol = None
        self.log = None
        self.qabul = []
        self.regis()

    def regis(self):
        a = input(self.ekran()).strip()
        os.system('cls')
        if self.fayl():
            while a not in ['1', '2']:
                os.system('cls')
                print('Iltimos aytilganlardan tanlang\n')
                a = input(self.ekran()).strip()
        else:
            while a not in ['1', '2', '3']:
                os.system('cls')
                print('Iltimos aytilganlardan tanlang\n')
                a = input(self.ekran()).strip()
        if a == '1':
            self.register()
        elif not self.fayl() and a == '2':
            self.login_()
        else:
            sys.exit()

    def register(self):
        self.log = input("Login: ").strip()
        self.parol = input("Password: ").strip()
        for i in range(len(self.log)):
            self.log.replace(' ', '')
        for i in range(len(self.parol)):
            self.parol.replace(' ', '')
        os.system('cls')

        while not self.uzun(self.log) or not self.uzun1(
                self.parol) or not self.log.isalnum() or not self.parol.isalnum() or self.sql_Login():
            os.system('cls')
            print("Iltimos belgi kiritmen, hato loginizda 3 tadan kam yoki passwordda 6 tadan kam\n")
            self.log = input("Login: ").strip()
            self.parol = input("Password: ").strip()
            for i in range(len(self.log)):
                self.log.replace(' ', '')
            for i in range(len(self.parol)):
                self.parol.replace(' ', '')

        name = input('Ismiz: ').strip()
        while not name.isalpha() or not self.ism(name):
            os.system('cls')
            print("Siz 3 tadan kam kirittiz yoki harif kiritmadiz\nIltimos togri yozin\n")
            name = input('Ismiz: ').strip()
        name = name.capitalize()

        years = input("Yoshiz: ").strip()
        while not years.isdigit() or not self.yosh(years):
            os.system('cls')
            print("Notogri siz 12 dan kotta bolishis kere\nIltimos togri yozin\n")
            years = input("Yoshiz: ").strip()

        Num = input("Tel:+998 ").strip()
        while not Num.isdigit() or not self.num(Num) or not int(Num) != 0:
            os.system('cls')
            print("Telefonizni kodi bilan yozin\nIltimos togri yozin\n")
            Num = input("Tel: +998").strip()

        print('Tabriklimiz\nAkkaunt ochildi!!!')
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS users(ID serial primary key, Login varchar(20), Password varchar(20), name VARCHAR(50), age int, numbers  varchar(20))")
        mycursor.execute(f"INSERT INTO users(Login, Password, name, age, numbers) VALUES('{self.log}', '{self.parol}', '{name}', '{years}', '+998{Num}')")


    def login_(self):
        self.log = input("Login: ").strip()
        self.parol = input("Password: ").strip()
        os.system("cls")
        if self.sql_Login() and self.sql_Password():
            os.system('cls')
            self.log_()
        else:
            print("Bunday akkaunt yoq")
            return self.login_()

    def log_(self):
        b = input("1 Malumot\n2 Akkauntni ochirish\n3 Loginni yangilash\n4 Passwordni yangilash\n5 Exit\n").strip()
        while b not in ['1', '2', '3', '4', '5']:
            os.system('cls')
            print("Iltimos\nAytilganlardan kiriting\n")
            b = input("1 Malumot\n2 Akkauntni ochirish\n3 Loginni yangilash\n4 Passwordni yangilash\n5 Exit\n").strip()
        os.system('cls')
        if b == '1':
            self.mal()
            self.log_()
        elif b == '2':
            self.ochirish()
            self.regis()
        elif b == '3':
            self.log_yangi(self.log)
        elif b == '4':
            self.password_yangi()
        else:
            sys.exit()


    def ochirish(self):
        mycursor = mydb.cursor()
        mycursor.execute(f"delete from users where Login='{self.log}'")

        os.system('cls')
        print("Akkaunt ochirildi")


    def log_yangi(self, sel):
        time_log = self.log
        self.log = input('New Login: ').strip()
        for i in range(len(self.log)):
            self.log.replace(' ', '')
        while not self.uzun(self.log) or not self.log.isalnum() or self.sql_Login():
            os.system('cls')
            print("Hato loginizda 3 tadan kam, yoki belgi kirittiz\n")
            self._log = input("New Login: ").strip()
            for i in range(len(self.log)):
                self.log.replace(' ', '')

        mycursor = mydb.cursor()
        mycursor.execute(f"update users set Login='{self.log}' where Login='{time_log}'")

        os.system('cls')
        print("Login yangilandi\n")


    def password_yangi(self):
        time_parol = self.parol
        self.parol = input('New Password: ').strip()
        for i in range(len(self.parol)):
            self.parol.replace(' ', '')
        while not self.uzun1(self.parol) or not self.parol.isalnum():
            os.system('cls')
            print("Hato passworda 6 tadan kam, yoki belgi bor\n")
            self.parol = input("New Password: ").strip()
            for i in range(len(self.parol)):
                self.parol.replace(' ', '')

        mycursor = mydb.cursor()
        mycursor.execute(f"update users set Password='{self.parol}' where Password='{time_parol}'")

        os.system('cls')
        print("Password yangilandi\n")


    def sql_Login(self):
        mycursor = mydb.cursor()
        mycursor.execute("select Login from users")
        a = mycursor.fetchall()
        for i in a:
            if i[0] == self.log:
                return True
        return False


    def sql_Password(self):
        mycursor = mydb.cursor()
        mycursor.execute("select Password from users")
        a = mycursor.fetchall()
        for i in a:
            if i[0] == self.parol:
                return True
        return False


    def mal(self):
        mycursor = mydb.cursor()
        mycursor.execute(f"select name, age, numbers from users where Login='{self.log}'")
        a = mycursor.fetchall()
        return print('Name:',a[0][0], '\nAge:', a[0][1], '\nNumber:', a[0][2])

    def ekran(self):
        if self.fayl():
            return """ 
            1 Register
            2 Exit
            """
        else:
            return """ 
            1 Register
            2 Login
            3 Exit
            """


    @staticmethod
    def fayl():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS users(ID serial primary key, Login varchar(20), Password varchar(20), name VARCHAR(50), age int, numbers  varchar(20))")
        mycursor = mydb.cursor()
        mycursor.execute("select * from users")
        a = mycursor.fetchall()
        if a == []:
            return True
        return False

    @staticmethod
    def yosh(y):
        return int(y) <= 100 and int(y) >= 12

    @staticmethod
    def num(y: str):
        return len(y) == 9

    @staticmethod
    def ism(y: str):
        return len(y) >= 3

    @staticmethod
    def uzun(log_: str):
        return 12 >= len(log_) and len(log_) >= 3

    @staticmethod
    def uzun1(parol_: str):
        return 6 <= len(parol_) and len(parol_) <= 12


d = register1()
mydb.commit()








