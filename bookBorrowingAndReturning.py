from datetime import *
import os
import tempfile
import shutil
import csv
import pandas as pd
import clientmanagment
from tkinter import *
from tkinter import messagebox
def menuwypozyczenia():
    def dodajksiazke():
        entries.append(entry.get())
        ListofBooks.insert(END,"Book with ID: " + entry.get())

    def wypozycz(): obsluga_wypozyczenia(str(entry1.get()),*entries)
    entries=[]
    wypoz = Tk()
    wypoz.geometry("300x300")
    wypoz.title("Wypozycz ksiazke")
    Label(wypoz,text = "Wpisuj wypozyczenia").pack(side=TOP,fill=BOTH)
    entry = Entry(wypoz,fg="red")
    entry.pack()
    Label(wypoz,text = "Wpisz id klienta").pack(side=TOP,fill=BOTH)
    entry1 = Entry(wypoz,fg="red")
    entry1.pack()
    nacisnij = Button(wypoz,text="Dodaj kolejna ksiazke",command=dodajksiazke)
    nacisnij.pack()
    zatwierdz = Button(wypoz,text="Zatwierdz",command = wypozycz)
    zatwierdz.pack()
    exit = Button(wypoz,text="exit",command= wypoz.destroy)
    exit.pack()
    scrollbar = Scrollbar(wypoz)
    scrollbar.pack(side=RIGHT, fill=Y)
    ListofBooks = Listbox(wypoz,yscrollcommand=scrollbar.set)
    ListofBooks.pack(side=BOTTOM,fill=BOTH)
    scrollbar.config(command=ListofBooks.yview)


def menuzwracania():
    def zwroc(): clientmanagment.return_book(entry1.get(),entry.get())
    wypoz = Tk()
    wypoz.geometry("300x300")
    wypoz.title("zwroc ksiazke")
    Label(wypoz,text = "Wpisuj wypozyczenia").pack(side=TOP,fill=BOTH)
    entry = Entry(wypoz,fg="red")
    entry.pack()
    Label(wypoz,text = "Wpisz id klienta").pack(side=TOP,fill=BOTH)
    entry1 = Entry(wypoz,fg="red")
    entry1.pack()
    zatwierdz = Button(wypoz,text="Zatwierdz",command = zwroc )
    zatwierdz.pack()

def zmien_status_ksiazki(bookid: str):
    """
        Function to manage book in process of returning
        books
    Args:
        bookid(str): ID of returned book

    Returns:
        Modified csv file with changed BORROWED,UPDATED status
        in book.cvs
    """
    filename = 'book.csv'
    tempfile.tempdir = os.getcwd()
    temp = tempfile.NamedTemporaryFile(
        mode='w', suffix=".csv", delete=False, encoding='utf-8')
    fields = ['ID', 'AUTHOR', 'TITLE', 'PAGES',
              "CREATED", "UPDATED", "BORROWED"]
    try:
        with open(filename, 'r') as csvfile, temp:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(temp, fieldnames=fields)
            for row in reader:
                if row['ID'] == bookid:
                    row['BORROWED'], row['UPDATED'], = "No", date.today()
                    row = {'ID': row['ID'], 'AUTHOR': row['AUTHOR'],
                           'TITLE': row['TITLE'], 'PAGES': row['PAGES'],
                           'CREATED': row['CREATED'],
                           'UPDATED': row['UPDATED'],
                           'BORROWED': row['BORROWED']}
                writer.writerow(row)
        if row is None:
            raise Exception("Nie bylo takiej ksiazki w bazie")
    except IOError as e:
        print("Problem with data stream", e)
    shutil.move(temp.name, filename)


def zmien_status_klienta(clientid: str, bookid: str):
    """
        Function to manage client in process of returning
        books
    Args:
        clientid(str): ID of client who's returning book
        bookid(str): ID of returned book

    Returns:
        Modified csv file with changed BORROWED,UPDATED,RETURN_DATE status
        in client's cvs
    """
    os.chdir("./DATABASE")
    filename = clientid + ".csv"
    tempfile.tempdir = os.getcwd()
    temp = tempfile.NamedTemporaryFile(
        mode='w', suffix=".csv", delete=False, encoding='utf-8')
    fields = ['ID', 'AUTHOR', 'TITLE', 'PAGES', "CREATED",
              "UPDATED", "BORROWED", "BORROWED_DATE", "RETURN_DATE"]
    try:
        with open(filename, 'r') as csvfile, temp:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(temp, fieldnames=fields)
            for row in reader:
                if row['ID'] == bookid:
                    row['BORROWED'], row['UPDATED'], row['RETURN_DATE'] = "No", date.today(
                    ), date.today()
                    row = {'ID': row['ID'], 'AUTHOR': row['AUTHOR'],
                           'TITLE': row['TITLE'], 'PAGES': row['PAGES'],
                           'CREATED': row['CREATED'], 'UPDATED': row['UPDATED'],
                           'BORROWED': row['BORROWED'], "BORROWED_DATE": row['BORROWED_DATE'],
                           'RETURN_DATE': row['RETURN_DATE']}
                writer.writerow(row)
    except IOError as e:
        print("Non-existent file", e)
    shutil.move(temp.name, filename)
    os.chdir("..")


def obsluga_wypozyczenia(clientid: str, *args):
    """
        Function that manages borrowing books from library
     Args:
         clientid (str): ID of client who's borrowing book
         *args: IDs of books that one want to borrow
     Returns:
         Modified csv file with changed BORROWED,UPDATED,BORROW_DATE status
         in client's cvs and modified book.csv with changed UPDATED,BORROWED
         columns of desired book
     """
    filename = 'book.csv'
    tempfile.tempdir = os.getcwd()
    temp = tempfile.NamedTemporaryFile(
        mode='w', suffix=".csv", delete=False, encoding='utf-8')
    fields = ['ID', 'AUTHOR', 'TITLE', 'PAGES',
              "CREATED", "UPDATED", "BORROWED"]
    df = pd.DataFrame()
    try:
        with open(filename, 'r') as csvfile, temp:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(temp, fieldnames=fields)
            for row in reader:
                for item in args:
                    if row['ID'] == item:
                        if row['BORROWED'] == "No":
                            row['BORROWED'], row['UPDATED'], = "Yes", date.today()
                            row = {'ID': row['ID'], 'AUTHOR': row['AUTHOR'], 'TITLE': row['TITLE'],
                                   'PAGES': row['PAGES'],
                                   'CREATED': row['CREATED'], 'UPDATED': row['UPDATED'], 'BORROWED': row['BORROWED']}
                            rowForClient = {'ID': row['ID'], 'AUTHOR': row['AUTHOR'], 'TITLE': row['TITLE'],
                                            'PAGES': row['PAGES'],
                                            'CREATED': row['CREATED'], 'UPDATED': row['UPDATED'],
                                            'BORROWED': row['BORROWED'],
                                            "BORROWED_DATE": str(date.today()), 'RETURN_DATE': "Nan"}
                            df = df.append(rowForClient, ignore_index=True)
                        else:
                            messagebox.showerror(message=str(item) + "Already borrowed")
                            exit(1)
                    writer.writerow(row)
    except IOError as e:
        print("Problem with data stream", e)
    shutil.move(temp.name, filename)
    os.chdir("./DATABASE")
    name = clientid + ".csv"
    df2 = pd.read_csv(name)
    df3 = pd.concat([df2, df], ignore_index=True)
    try:
        df3.to_csv(name, index=False)
    except ConnectionError as e:
        print("Database unavailable to read", e)
    os.chdir("..")
