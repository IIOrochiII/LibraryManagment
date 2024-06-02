import pandas as pd
import random
import datetime
from tkinter import *
'''
NAME
    toolsbook

DESCRIPTION
    This module is designed to add and remove entires to library data base
    using basic values (id,author,name title,pages,created,updated )
    
    Files given to this module must be written in (.csv) format
    This script requires pandas to be installed with the Python environment 
    you are working with.
    
FUNCTIONS
    This module contains the following functions:
    
    *choose_option(fun,**kwargs) - manages ad_record and remove_record
    functions by accepting them as parameter and kwargs which they take
    
    * ad_record(**kwargs) - adds entry to .csv
    file by using pandas and date 

    * remove_record(**kwargs) - deletes entry from .csv
    file by giving IDs or TITILES of book in database 
    
EXAMPLES
    add_record(ID = "223",AUTHOR = "Jason Nowak",
               TITLE = "Nightmare of the previous friday", PAGES = 233,
               CREATED = date.today(), UPDATED = date.today(),BORROWED = "No)
               
    remove_record(ID = 223,TITLE = "Nightmare of the previous friday")
    
    choose_option(add_record,ID = "223",AUTHOR = "Jason Nowak",
               TITLE = "Nightmare of the previous friday", PAGES = 233,
               CREATED = date.today(), UPDATED = date.today(),BORROWED = "No)
               
    choose_option(remove_record,ID = "223",TITLE = "Nightmare of the previous friday")
'''
def menuofaddingremovingbooks():
    def call_add():
        def add(): add_record(ID=entry1.get(), AUTHOR=entry2.get(), TITLE=entry3.get(),
                              PAGES=entry4.get(), CREATED=datetime.date.today(), UPDATED=datetime.date.today(),
                              BORROWED="No")

        new_window = Tk()
        new_window.title("Podaj dane")
        new_window.geometry("500x200")
        text1 = Label(new_window, text="ID")
        text2 = Label(new_window, text="AUTOR")
        text3 = Label(new_window, text="TYTUL")
        text4 = Label(new_window, text="STRONY")
        entry1 = Entry(new_window, fg="black")
        entry2 = Entry(new_window, fg="black")
        entry3 = Entry(new_window, fg="black")
        entry4 = Entry(new_window, fg="black")
        text1.pack(side=TOP, expand=True)
        entry1.pack(side=TOP, expand=True)
        text2.pack(side=TOP, expand=True)
        entry2.pack(side=TOP, expand=True)
        text3.pack(side=TOP, expand=True)
        entry3.pack(side=TOP, expand=True)
        text4.pack(side=TOP, expand=True)
        entry4.pack(side=TOP, expand=True)
        Ok = Button(new_window, text='OK', command=add)
        Ok.pack(side=BOTTOM)
        exit = Button(new_window, text="Exit", command=new_window.destroy)
        exit.pack(side=BOTTOM)
        new_window.mainloop()
    def usunIdlubTytul():
        def usun():  remove_record(ID=int(entry.get()), TITLE=entry.get())
        wprowadzid = Tk()
        wprowadzid.title("Wprowadz id lub imie")
        text = Label(wprowadzid, text="wprowadz id lub imie")
        entry = Entry(wprowadzid, fg='red')
        ok = Button(wprowadzid, text="Ok", fg="red", command=usun)
        exit = Button(wprowadzid, text="exit", fg="red", command=wprowadzid.destroy)
        text.pack(expand=True)
        entry.pack(expand=True)
        ok.pack(expand=True)
        exit.pack(expand=True)
        wprowadzid.geometry("200x200")
        wprowadzid.mainloop()

    manage = Tk()
    manage.title("Wybierz opcje")
    manage.geometry("200x200")
    opcja_dodaj = Button(manage, text="Dodaj Ksiazke", command=call_add)
    opcja_usun = Button(manage, text="Usun Ksiazke", command=usunIdlubTytul)
    exit = Button(manage, text="Exit", command=manage.destroy)
    opcja_dodaj.pack(expand=True)
    opcja_usun.pack(expand=True)
    manage.mainloop()


def choose_option(fun, **kwargs):
    return fun(**kwargs)


# def add_record(author:str,title:str,pages:int):
#     df= pd.read_csv("book.csv")
#     bookID = 101 + len(df.index)
#     created = date.today()
#     df2= pd.DataFrame({"ID":[bookID],"AUTHOR":[author],"TITLE":[title],
#                        "PAGES":[pages],"CREATED":[created],"UPDATED":[created],
#                        "BORROWED":["No"]}, )
#     df3 = pd.concat([df, df2], ignore_index=True)
#     df3.to_csv("book.csv",index=False)
#     return


def add_record(**kwargs):
    df = pd.read_csv("book.csv")
    while df.loc[(df['ID'] == kwargs["ID"])].any().all():
        kwargs["ID"] = random.randint(100, 999)
    df2 = pd.DataFrame([kwargs])
    df3 = pd.concat([df, df2], ignore_index=True)
    df3.to_csv("book.csv", index=False)
    return


# Unless the entries in your index are of uniform length,
# (so the final character is always the same number of bytes from the start of the line),
# I think it is necessary to rewrite every line.
# Just one of the unfortunate downsides of working with a text-based format like csv.


def remove_record(**kwargs):
    df = pd.read_csv("book.csv",skip_blank_lines=True)
    for key,value in kwargs.items():
        df.drop(df.index[(df[key] == value)], axis=0, inplace=True)
    df.to_csv("book.csv", index=False)
    return
