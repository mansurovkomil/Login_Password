


import os
import sys


class register1:
    def __init__(self):
        self.parol=None
        self.log=None
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
        if a=='1':
            self.register()
        elif not self.fayl() and a=='2':
            self.login_()
        else:
            sys.exit()

    def register(self):
        self.log=input("Login: ").strip()
        self.parol=input("Password: ").strip()
        for i in range(len(self.log)):
            self.log.replace(' ', '')
        for i in range(len(self.parol)):
            self.parol.replace(' ', '')
        os.system('cls')

        while not self.uzun(self.log) or not self.uzun1(self.parol) or not self.log.isalnum() or not self.parol.isalnum() or self.bormi(self.log):
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

        years = input("Yoshiz: ").strip()
        while not years.isdigit() or not self.yosh(years):
            os.system('cls')
            print("Notogri siz 12 dan kotta bolishis kere\nIltimos togri yozin\n")
            years = input("Yoshiz: ").strip()

        Num = input("Tel: ").strip()
        while not Num.isdigit() or not self.num(Num):
            os.system('cls')
            print("Telefonizni kodi bilan yozin\nIltimos togri yozin\n")
            Num = input("Tel: +998").strip()

        print('Tabriklimiz\nAkkaunt ochildi!!!')

        j = open("registr.txt", 'a')
        j.write(f"Login:"+self.log + "|Password:"+self.parol+ "/name="+name.capitalize() +'-years='+ str(int(years)) +'>Num=+998'+ Num+ "\n")


    def login_(self):
        s = 0
        self.log = input("Login: ").strip()
        self.parol = input("Password: ").strip()
        self.koesh()
        os.system("cls")
        for i in self.qabul:
            if i["Login"] == self.log and i["Password"] == self.parol:
                s=1

        if s == 1:
            os.system('cls')
            self.log_()
        else:
            print("Bunday akkaunt yoq")
            return self.login_()

    def log_(self):
        b = input("1 Malumot\n2 Akkauntni ochirish\n3 Loginni yangilash\n4 Passwordni yangilash\n").strip()
        while b not in ['1', '2', '3', '4']:
            os.system('cls')
            print("Iltimos\nAytilganlardan kiriting\n")
            b = input("1 Malumot\n2 Akkauntni ochirish\n3 Loginni yangilash\n4 Passwordni yangilash\n").strip()
        os.system('cls')
        if b == '1':
            self.mal()
            self.log_()
        elif b == '2':
            self.ochirish()
        elif b == '3':
            self.log_yangi(self.log)
        else:
            self.password_yangi()


    def koesh(self):
        with open('registr.txt') as f:
            k = f.read().split()
            for g in k:
                self.qabul.append(
                    {
                        'Login': g.split('|')[0].split(':')[1],
                        'Password': g.split('|')[1].split(':')[1].split('/')[0],
                        'Mal': g.split('/')[1].split('-')[0],
                        'Malum': g.split('/')[1].split('-')[1].split('>')[0],
                        'Malumot1': g.split('/')[1].split('-')[1].split('>')[1]
                    }
                )


    def ochirish(self):
        v = open('registr.txt')
        v1 = v.read().split()
        h = open("registr.txt", 'w')
        h.write('')
        for i in v1:
            if i.split('|')[0].split(':')[1] == self.log:
                pass
            else:
                h = open("registr.txt", 'a')
                h.write(i + '\n')
                h.close()
        self.koesh()
        os.system('cls')
        print("Akkaunt ochirildi")


    def log_yangi(self, sel):
        time_log = input('New Login: ').strip()
        for i in range(len(self.log)):
            self.log.replace(' ', '')
        while not self.uzun(time_log) or not time_log.isalnum() or self.bormi(time_log):
            os.system('cls')
            print("Hato loginizda 3 tadan kam, yoki belgi kirittiz\n")
            time_log = input("New Login: ").strip()
            for i in range(len(self.log)):
                self.log.replace(' ', '')

        v = open('registr.txt')
        v1 = v.read().split()
        h = open("registr.txt", 'w')
        h.write('')
        for i in v1:
            if i.split('|')[0].split(':')[1] == sel:
                h = open("registr.txt", 'a')
                h.write(f'Login:'+time_log+'|'+i.split('|')[1]+'\n')
                h.close()
            else:
                h = open("registr.txt", 'a')
                h.write(i+'\n')
                h.close()
        self.koesh()
        os.system('cls')
        print("Login yangilandi\n")


    def password_yangi(self):
        time_parol = input('New Password: ').strip()
        for i in range(len(self.parol)):
            self.parol.replace(' ', '')
        while not self.uzun1(time_parol) or not time_parol.isalnum() and self.bormi(time_parol):
            os.system('cls')
            print("Hato passworda 6 tadan kam, yoki belgi bor\n")
            time_parol = input("New Password: ").strip()
            for i in range(len(self.parol)):
                self.parol.replace(' ', '')

        v = open('registr.txt')
        v1 = v.read().split()
        h = open("registr.txt", 'w')
        h.write('')
        for i in v1:
            if i.split('|')[0].split(':')[1] == self.log:
                h = open("registr.txt", 'a')
                h.write(f''+i.split('|')[0]+'|Password:'+time_parol+'/'+i.split('|')[1].split(':')[1].split('/')[1]+'\n')
                h.close()
            else:
                h = open("registr.txt", 'a')
                h.write(i+'\n')
                h.close()
        self.koesh()
        os.system('cls')
        print("Password yangilandi\n")

    def mal(self):
        for i in self.qabul:
            if i['Login']==self.log and i['Password']==self.parol:
                return print(i['Mal']+'\n'+i['Malum']+'\n'+i['Malumot1'])


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
        k=open("registr.txt")
        return k.read()==''

    @staticmethod
    def yosh(y):
        return int(y)<=100 and int(y)>=12

    @staticmethod
    def num(y: str):
        return len(y)==9

    @staticmethod
    def ism(y: str):
        return len(y)>=3

    @staticmethod
    def uzun(log_: str):
        return 12>=len(log_) and len(log_)>=3

    @staticmethod
    def uzun1(parol_: str):
        return 6<=len(parol_) and len(parol_)<=12

    def bormi(self, k):
        self.koesh()
        for i in self.qabul:
            if i['Login'] == k:
                return True
        return False


d = register1()










