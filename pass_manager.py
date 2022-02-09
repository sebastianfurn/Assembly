import psycopg2
from getpass import getpass
import array
from tkinter import Tk
import os

password = getpass()

def ins_pass():
    try:
        con = psycopg2.connect("dbname='glass' user='postgres' host='localhost' password='{}'".format(password))
        cur = con.cursor()
        insert_sql = "INSERT INTO great(username,password,email,url,site_name) values (%s,%s,%s,%s,%s)"
        my_values = []
        my_values.append(input("Username: "))
        my_values.append(getpass())
        my_values.append(input("Email: "))
        my_values.append(input("URL: "))
        my_values.append(input("Site : "))
        cur.execute(insert_sql, my_values)
        con.commit()
        print()
        print("*** You successfully inserted your data! ***")
        con.close()
    except (Exception, psycopg2.Error) as error:
        print()
        print(error)

def get_pass():
    try:
        con = psycopg2.connect("dbname='glass' user='postgres' host='localhost' password='{}'".format(password))
        cur = con.cursor()
        site = input("Site: ")
        insert_sql = "SELECT password FROM great WHERE site_name = %s"
        sites = []
        sites.append(site)
        cur.execute(insert_sql, sites)
        data = cur.fetchall()[0][0]
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(data)
        r.update()
        print()
        print("*** Your password has been copied to clipboard ***")
        con.close()
    except (Exception, psycopg2.Error) as error:
        print()
        print(error)

def menu():
    print()
    print('-'*30, " MENU ", '-'*30)
    print("* Press 1 to insert new password")
    print("* Press 2 to get password from site")
    print("* Press 3 to exit program")
    print('-'*68)


while(True):
    os.system('clear' if os.name == "posix" else "cls")
    menu()
    choice = input(": ").strip()
    if(choice == '1'):
        ins_pass()
    elif(choice == '2'):
        get_pass()
    elif(choice == '3'):
        os.system('clear' if os.name == "posix" else "cls")
        break
    else:
        print()
        print("*** Your input is invalid ***")
    input()

