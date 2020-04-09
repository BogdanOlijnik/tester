#! /usr/bin/python3

from funcDB import *
import argparse

parser = argparse.ArgumentParser(
    description='Parser to migration people list to data base')
parser.add_argument('--install-mysql', dest="installMysql",
                    default=None, type=str, help="install-mysql", required=False)
parser.add_argument('--create-dataBase', dest="createDataBase",
                    default=None, type=str, help="create data base", required=False)
parser.add_argument('--create-table', dest="createTable", default=None,
                    type=str, help="create data table", required=False)
parser.add_argument('--drop-dataBase', dest="dropDataBase",
                    default=None, type=str, help="drop data base", required=False)
parser.add_argument('--drop-table', dest="dropTable", default=None,
                    type=str, help="drop data table", required=False)
parser.add_argument('--dataBaseName', dest="dataBaseName",
                    type=str, help="Name of data base to use", required=False)
parser.add_argument('--tableName', dest="tableName", type=str,
                    help="Name of table to use", required=False)
parser.add_argument('--fileSchema', dest="fileSchema",
                    default=None, type=str, help="fileSchema", required=False)
parser.add_argument('--migration', dest="migrationOfDatabase", default=None,
                    type=str, help="migration to data base", required=False)
parser.add_argument('--people-list', dest="peopleList", type=str,
                    help="path to file with people list", required=False)
parser.add_argument('--people-outlist', dest="peopleOuthList", type=str,
                    help="path to file with generate of people list", required=False)
parser.add_argument('--ip-addres', dest="ipAddress", default=None,
                    type=str, help="ip to remote mySql", required=False)
parser.add_argument('--username', dest="userName", default=None,
                    type=str, help="name of user to mySql", required=False)
parser.add_argument('--password', dest="password", default=None,
                    type=str, help="password of user to mySql", required=False)
parser.add_argument('--id', dest="id", type=int,
                    help="Id in the table", required=False)
parser.add_argument('--lastname', dest="lastname",
                    default=None, type=str, help="lastname", required=False)
parser.add_argument('--name', dest="name", default=None,
                    type=str, help="name", required=False)
parser.add_argument('--fathername', dest="fathername", type=str,
                    help="fathername", required=False)
parser.add_argument('--email', dest="email", type=str,
                    help="email", required=False)
parser.add_argument('--age', dest="age", default=None,
                    type=int, help="age", required=False)
parser.add_argument('--phone', dest="phone", default=None,
                    type=str, help="phone", required=False)
parser.add_argument('--salary', dest="salary", default=None,
                    type=int, help="salary", required=False)
args = parser.parse_args()
installSql = args.installMysql
createDB = args.createDataBase
createTable = args.createTable
dropdb = args.dropDataBase
droptable = args.dropTable
dbName = args.dataBaseName
tableName = args.tableName
schema = args.fileSchema
migration = args.migrationOfDatabase
peopleList = args.peopleList
peopleOutList = args.peopleOuthList
ip = args.ipAddress
user = args.userName
passwd = args.password
id = args.id
lastname = args.lastname
name = args.name
fathername = args.fathername
email = args.email
age = args.age
phone = args.phone
salary = args.salary


def main():
    if peopleList != None and peopleOutList != None and ip != None and user != None and passwd != None and dbName != None and tableName != None:
        mainMigration(ip, dbName, tableName, user,
                      passwd, peopleList, peopleOutList)
    elif id != None and lastname != None and name != None and fathername != None and email != None and age != None and phone != None and salary != None and ip != None and user != None and passwd != None and dbName != None and tableName != None:
        writeDB(ip, dbName, tableName, user, passwd, id, lastname,
                name, fathername, email, age, phone, salary)
    elif createDB == "yes" and ip != None and user != None and passwd != None and dbName != None and tableName != None:
        create(ip, dbName, tableName, user, passwd)
    elif droptable == "yes" and ip != None and user != None and passwd != None and dbName != None and tableName != None:
        dropTable(ip, dbName, tableName, user, passwd)
    elif dropdb == "yes" and ip != None and user != None and passwd != None and dbName != None:
        dropDB(ip, dbName, user, passwd)


main()
