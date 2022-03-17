



import os


class uzer:

    def __init__(self, b, login, pas):
        self.b1 = b
        self.log1=login
        self.pas1=pas

    def ozlash(self):
        s = 0
        if self.b1 == '2':
            k = open("registr.txt")
            h = k.read().split()
            for i in range(0, len(h), +2):
                if h[i] == self.log1 and h[i + 1] == self.pas1:
                    s = s + 1
            if s == 0:
                k = open("registr.txt", "a")
                k.write(self.log1 + "\n" + self.pas1 + "\n")
                print("Registratsiyadan muvafaqiyatli o'tdingiz✍️🖇")
            else:
                print("Bunday akkaunt bant")
        else:
            k = open("registr.txt")
            h = k.read().split()
            for i in range(0, len(h), +2):
                if h[i]==self.log1 and h[i+1]==self.pas1:
                    print('ID:'+ str(i//2+1) +'\n'+h[i],"\n",h[i+1])
                    s=s+1
            if s==0:
                print("Bunday Akkaunt yoq")


a = '2'

while True:
    # if a=='2':
    #     os.system("cls")
    a = input("1 Login\n" "2 register \n")

    while a not in ["1", "2"]:
        os.system("cls")
        a = input("Hato kirittiz.\n1 Login\n" "2 register \n")

    log = input("Login: ")
    passvord = input("Password: ")

    while ' ' in passvord or ' ' in log:
        os.system('cls')
        print("hato kirittingiz")
        log = input("Login: ")
        passvord = input("Password: ")

    s = uzer(a, log, passvord)
    s.ozlash()











