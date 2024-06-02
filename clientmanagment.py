import random
import pandas as pd
from datetime import *
import os
import csv
import bookBorrowingAndReturning
import RemovingClient
from tkinter import *
from tkinter import messagebox
'''
NAME
    clientmanagment

DESCRIPTION
    This module contains functions to manage clients that are in database
    of library

    This script requires pandas,datetime and csv to be installed within
    the Python environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    * manage_client() - this function calls a menu for user to choose which
    action they want to do. Add new client or delete already existing one

    * add_client(name: str, surname: str, email: str,
    phone: str, street: str, city: str, country: str) - by using this function
    one can add a new record to .csv file that has records of clients

    *remove_client(clientid:int) - this function is designed
    to completly remove client from database, it deletes
    record in address.cvs, customer.csv and record from
    DATABASE directory

    *borrow_book(clientid: str,*args) - function used
    to register books that customer borrows from library

    *return_book(clientid:str,*args) - by using this function you
    note returning of book from client it changes record in
    cvs that belongs to customer DATABASE folder and changes
    columns BORROWED,UPDATED,RETURN_DATE in specific cvs

EXAMPLES
    add_client("Arthur","LeonHeart","ArthurL@gmail.com",
               "730878222","Witchshouse","London","GB")

    remove_client("1234")

    borrow_book("1234","111","112","132")

    return_book("1234","111","112","132")
'''



def manage_client():

    def call_1():
        def add(): add_client(entry1.get(), entry2.get(), entry3.get(),
                              entry4.get(), entry5.get(), entry6.get(),
                              entry7.get())

        new_window = Tk()
        new_window.title("Podaj dane")
        new_window.geometry("500x200")
        text1 = Label(new_window,text="Imie")
        text2 = Label(new_window,text="Nazwisko")
        text3 = Label(new_window,text="Email")
        text4 = Label(new_window,text="Phone")
        text5 = Label(new_window,text="Street")
        text6 = Label(new_window,text="City")
        text7 = Label(new_window,text="Country")
        entry1 = Entry(new_window,fg="black")
        entry2 = Entry(new_window,fg="black")
        entry3 = Entry(new_window,fg="black")
        entry4 = Entry(new_window,fg="black")
        entry5 = Entry(new_window,fg="black")
        entry6 = Entry(new_window,fg="black")
        entry7 = Entry(new_window,fg="black")
        text1.pack(side=TOP,expand =True)
        entry1.pack(side=TOP,expand=True)
        text2.pack(side=TOP,expand=True)
        entry2.pack(side=TOP,expand = True)
        text3.pack(side=TOP,expand=True)
        entry3.pack(side=TOP,expand = True)
        text4.pack(side=TOP,expand=True)
        entry4.pack(side=TOP,expand = True)
        text5.pack(side=TOP,expand = True)
        entry5.pack(side=TOP,expand = True)
        text6.pack(side=TOP,expand = True)
        entry6.pack(side=TOP,expand = True)
        text7.pack(side=TOP,expand = True)
        entry7.pack(side=TOP,expand=True)
        Ok = Button(new_window,text='OK',command= add)
        Ok.pack(side=BOTTOM)
        exit = Button(new_window,text="Exit",command= new_window.destroy)
        exit.pack(side=BOTTOM)
        new_window.mainloop()

    def opcja1():
        def usunId():  RemovingClient.remove_client_by_id(int(entry.get()))
        wprowadzid = Tk()
        wprowadzid.title("Wprowadz id")
        text = Label(wprowadzid,text = "wprowadz id")
        entry = Entry(wprowadzid,fg='red')
        ok = Button(wprowadzid,text="Ok",fg="red",command= usunId)
        exit = Button(wprowadzid,text ="exit",fg="red",command= wprowadzid.destroy)
        text.pack(expand=True)
        entry.pack(expand=True)
        ok.pack(expand=True)
        exit.pack(expand=True)
        wprowadzid.geometry("200x200")
        wprowadzid.mainloop()
    def opcja2():
        def usunImie(): RemovingClient.remove_client_by_name(entry.get())
        wprowadzimie = Tk()
        wprowadzimie.title("Wprowadz imie")
        text = Label(wprowadzimie,text = "wprowadz imie")
        entry = Entry(wprowadzimie,fg='red')
        ok = Button(wprowadzimie,text="Ok",fg="red",command= usunImie)
        exit = Button(wprowadzimie,text="Exit",fg="red",command= wprowadzimie.destroy)
        text.pack(expand=True)
        entry.pack(expand=True)
        ok.pack(expand=True)
        exit.pack(expand=True)
        wprowadzimie.geometry("200x200")
        wprowadzimie.mainloop()
    def call2():
        newwindow = Tk()
        newwindow.title("Wybierz opcje")
        newwindow.geometry("500x200")


        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        C1 = Checkbutton(newwindow,text="ID",variable = CheckVar1,
                         onvalue = 1,offvalue = 0,height = 5,
                         width = 20,command=opcja1)
        C2 = Checkbutton(newwindow,text="Imie",variable = CheckVar2,
                         onvalue = 1,offvalue = 0,height = 5,
                         width = 20,command=opcja2)
        C1.pack()
        C2.pack()
        exit = Button(newwindow,text="Exit",command= newwindow.destroy)
        exit.pack(side=BOTTOM)
        newwindow.mainloop()

    manage = Tk()
    manage.title("Wybierz opcje")
    manage.geometry("200x200")
    opcja_dodaj= Button(manage,text = "Dodaj Klienta",command=call_1)
    opcja_usun= Button(manage,text = "Usun Klienta",command=call2)
    exit = Button(manage,text="Exit",command= manage.destroy)
    opcja_dodaj.pack(expand=True)
    opcja_usun.pack(expand=True)
    manage.mainloop()


def add_client(name: str, surname: str, email: str,
               phone: str, street: str, city: str, country: str):
    df = pd.read_csv("customer.csv")
    # if df.loc[(df['NAME'] == name + " " + surname)].any().all() and df.:
    #     raise Exception("Klient znajduje sie w bazie")
    clientid = random.randint(1000, 9999)
    while df.loc[(df['ID'] == clientid)].any().all():
        clientid = random.randint(1000, 999)
    df2 = pd.DataFrame({"ID": [clientid], "NAME": [
        name + " " + surname], "E-MAIL": [email], "PHONE": [phone],
                        "CREATED": [date.today()], "UPDATED": [date.today()]})
    df3 = pd.concat([df, df2], ignore_index=True)
    df3.to_csv("customer.csv", index=False)
    df_address = pd.read_csv("address.csv")
    df_address_2 = pd.DataFrame({"ID": [clientid], "STREET": [street],
                                 "CITY": [city], "COUNTRY": country})
    df_address_3 = pd.concat([df_address, df_address_2], ignore_index=True)
    df_address_3.to_csv("address.csv", index=False)
    os.chdir("./DATABASE")
    name_of_file = str(clientid) + ".csv"
    headerList = ['ID', 'AUTHOR', 'TITLE', 'PAGES', "CREATED",
                  "UPDATED", "BORROWED", "BORROWED_DATE", "RETURN_DATE"]
    with open(name_of_file, 'w') as file:
        dw = csv.DictWriter(file, delimiter=',', fieldnames=headerList)
        dw.writeheader()
    os.chdir("..")



def borrow_book(clientid: str, *args):
    bookBorrowingAndReturning.obsluga_wypozyczenia(clientid, *args)


def return_book(fun):
    def wrapper(clientid:int, *args):
        for item in args:
            bookBorrowingAndReturning.zmien_status_ksiazki(item)
            bookBorrowingAndReturning.zmien_status_klienta(clientid, item)
    return wrapper


@return_book
def return_book(clientid: str, bookid: str):
    bookBorrowingAndReturning.zmien_status_ksiazki(bookid)
    bookBorrowingAndReturning.zmien_status_klienta(clientid, bookid)
