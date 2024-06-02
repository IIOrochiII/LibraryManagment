import PIL.Image

from clientmanagment import *
from toolsbook import *
from tkinter import *
import pickle
from PIL import Image, ImageTk
import requests
from bookBorrowingAndReturning import *
from ocen import *


def biblioteka():
    url = "https://img.freepik.com/free-vector/hand-drawn-flat-design-stack-books_23-2149334862.jpg?size=338&ext=jpg&ga=GA1.1.2082370165.1717027200&semt=sph"
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open("sample.jpg", "wb") as f:
            f.write(response.content)

    window = Tk()
    window.title("Obsluga biblioteki")
    window.geometry("700x500")
    opcja_1 = Button(text="Zarzadaj Klientem", bg="green", command=manage_client)
    opcja_2 = Button(text="Dodaj/Usun Ksiazke", bg="green", command=menuofaddingremovingbooks)
    opcja_4 = Button(text="Wypozycz Ksiazke", bg="green", command=menuwypozyczenia)
    opcja_5 = Button(text="Zwroc ksiazke", bg="green", command=menuzwracania)
    opcja_6 = Button(text="Wyjdz z programu", fg='red', command=window.destroy)
    opcja_7 = Button(text="Ocen Program", fg='red', command=ocen)
    opcja_1.pack(side=TOP, expand=True, fill=BOTH)
    opcja_2.pack(side=TOP, expand=True, fill=BOTH)
    opcja_4.pack(side=TOP, expand=True, fill=BOTH)
    opcja_5.pack(side=TOP, expand=True, fill=BOTH)
    opcja_6.pack(side=LEFT, expand=True, fill=BOTH)
    opcja_7.pack(side=LEFT, expand=True, fill=BOTH)
    bgofbiblio = PIL.Image.open("sample.jpg")
    logo1 = ImageTk.PhotoImage(bgofbiblio)
    logo2 = Label(image=logo1)
    logo2.image = logo1
    logo2.pack(fill=BOTH)
    window.mainloop()


if __name__ == '__main__':
    biblioteka()
