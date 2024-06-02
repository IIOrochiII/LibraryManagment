from tkinter import *
import pickle
def ocen():
    def return_result():
        result = "Oceniles program na " + str(varscale.get())
        with open("ocena.data", "wb") as filee:
            pickle.dump(result, filee)

    ocena = Tk()
    ocena.title("Ocen dzialanie")
    ocena.geometry("300x300")
    Label(ocena, text="Ocena", bg="green", fg="white").pack()
    varscale = IntVar()
    suwak = Scale(ocena, orient="horizontal", variable=varscale, from_=0, to=5, )
    suwak.pack(anchor=CENTER)
    Button(ocena, text="Ocen", command=return_result).pack()
    Button(ocena, text="wyjdz", command=ocena.destroy).pack()
    ocena.mainloop()