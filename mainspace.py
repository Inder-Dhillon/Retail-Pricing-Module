from tkinter import *
from bs4 import BeautifulSoup
from requests import get
from bs4 import SoupStrainer
from lxml import *


root = Tk()
root.title("Factory Direct")
root.geometry("600x400")


#Functions
def retrieve(event):
    a1 = barcode.get()
    # URL Control
    url = "https://www.factorydirect.ca/productsearch/upcs?q="+a1+"&barcode=1"
    r = get(url).text
    only_div = SoupStrainer('div')
    soup = BeautifulSoup(r, "lxml", parse_only=only_div)
    #Catch-hold for the Yellow Tag Bug
    discounttag = soup.find('span', {"class": "yellow-save"})
    prodname = soup.find('div', {"class": "product-name"})
    prodcondition = soup.find('div', {"class": "modelno"})
    saletag = soup.find('div', {"class": "red-box"})
    if discounttag is not None:
        price1 = discounttag.find_next('span').get_text()
        price1 = price1[:-2] + ".99"
        label1["text"] = price1
        nameprod["text"] = prodname.get_text(strip=TRUE)

        if prodcondition.get_text(strip=TRUE) != "":
            cdn["text"] = prodcondition.get_text(strip=TRUE)
            cdn["bg"] = "black"

        else:
            cdn["text"] = "Certified Refurbished"
            cdn["bg"] = "black"

    else:
        pricetag = soup.find('div', {"class": "big-price-details"})
        if pricetag is None:
            nameprod["text"] = ""
            label1["text"] = "Not Found"
            sale["text"] = ""
            sale["bg"] = "white"
            cdn["text"] = ""
            cdn["bg"] = "white"
        else:
            price1 = pricetag.get_text()
            price1 = price1[:-2] + "." + price1[-2:]
            label1["text"] = price1
            nameprod["text"] = prodname.get_text(strip=TRUE)
            sale["text"] = ""
            sale["bg"] = "white"
            if prodcondition.get_text(strip=TRUE) != "":
                cdn["text"] = prodcondition.get_text(strip=TRUE)
                cdn["bg"] = "black"

            else:
                cdn["text"] = "Certified Refurbished"
                cdn["bg"] = "black"
    if saletag is not None:
        sale["text"] = "  On Sale  "
        sale["bg"] = "#e00119"
    barcode.selection_range(0, END)


#GUI
root["bg"] = "white"
Label(root, text="Barcode:", font="Roboto", bg="white").pack(pady=7)
barcode = Entry(root, justify=CENTER, bg="#dcdcdc", width=80, borderwidth=0)
barcode.pack()
barcode.bind("<Return>", retrieve)
nameprod = Label(root, text="", font=("Roboto", 13), bg="white")
nameprod.pack(padx=1)
cdn = Label(root, text="", font=("Roboto", 10), bg="white", fg="white")
cdn.pack()
label1 = Label(root, text="", font=("Roboto", 90), bg="white")
label1.pack()
sale = Label(root, text="", font=("Roboto", 25), bg="white", fg="white")
sale.pack()
creditsforfrx = Label(root, text="Ver 1.01-Ferox")
creditsforfrx.pack(pady=40)
root.mainloop()