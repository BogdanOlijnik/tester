#! /usr/bin/python3
# coding: CP1251
import codecs
import csv
import random
import sys

def mainGen(initial, ending):
    def genEmeil():  # функція генерування пошти
        str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        head = ''.join([random.choice(str1) for x in range(6)])
        strtemp = ['@ukr.net', '@gmail.com', '@i.ua', '@mil.gov', '@dod.ua']
        tail = strtemp[random.randrange(0,len(strtemp))]
        return "{0}{1}".format(head,tail)


    def genPhone():  # функція генерування номера телефона
        str1 = '1234567890'
        tail = ''.join([random.choice(str1) for x in range(7)])
        strtemp = ['+38050', '+38063', '+38066', '+38067', '+38091']
        head = strtemp[random.randrange(0,len(strtemp))]
        return "{0}{1}".format(head,tail)


    def genAge():  # функція генерування віку
        age = random.randint(20, 80)
        return(age)


    def genSalary():  # функція генерування зарплати
        salary = random.randint(5000, 100000)
        return(salary)

    peoplemas = []
    with codecs.open(initial, "r", encoding='CP1251') as FILENAME:
        reader = csv.reader(FILENAME)
        for row in reader:
            a = row[0]                # присвоює змінній значення першого елемента рядка
            b = a.split(";")          # розбиває цей елемент на частини по ";"
            value1 = b[0]             # присвоює першу частину змінній
            c = b[1]                  # присвоює другу частину змінній
            lst = c.split(" ")        # розбиває другу частину на елементи по пробілу
            value2 = lst[0]           # присвоює перший елемент змінній
            value3 = lst[1]           # присвоює другий елемент змінній
            value4 = lst[2]           # присвоює третій елемент змінній
            value5 = genEmeil()       # присвоює змінній згенеровану пошту
            value6 = genAge()         # присвоює змінній згенерований вік
            value7 = genPhone()       # присвоює змінній згенерований номер телефону
            value8 = genSalary()      # присвоює змінній згенеровану зарплату
            peoplemas.append({
                'ID':value1,
                'LASTNAME':value2,
                'NAME':value3,
                'FATHERNAME':value4,
                'EMAIL':value5,
                'AGE':value6,
                'PHONE':value7,
                'SALARY':value8

            })

            with open(ending, 'a', newline='') as file1:
                fieldnames = ['id', 'lastname', 'name', 'fathername', 'email', 'age', 'phone', 'salary']
                #writer = csv.writer(file, delimiter = ',')
                writer = csv.DictWriter(file1, fieldnames=fieldnames)
                #writer.writeheader()
                writer.writerow({'id': value1, 'lastname': value2, 'name': value3, 'fathername': value4, 'email': value5, 'age': value6, 'phone': value7, 'salary': value8})

    return peoplemas

#mainGen(initial, ending)
#initial = "/home/bohdan/project/people.csv"
#ending = "/home/bohdan/project/generatedPeople.csv"
#a = mainGen(initial, ending)
#for i in a:
    #print("ID:{0} LASTNAME:{1} NAME:{2} FATHERNAME:{3} EMAIL:{4} AGE:{5} PHONE:{6} SALARY:{7}")

