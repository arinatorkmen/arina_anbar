from tkinter import *
from tkinter.ttk import *
from anbar.controller.StuffController import StuffController


class StuffUI:
    def __init__(self):
        print("stuffView")
        labels = ['Code', 'Name', 'Unit', 'Count', 'Price']

        self.window = Tk()
        self.window.title("Stuff")
        self.window.geometry("600x250")

        y = 20
        for lb in labels:
            # lbl = Label(self.window, text=lb).place(x=20, y=y)
            Label(self.window, text=lb).place(x=20, y=y)
            y += 30

        self.code_txt = Entry(self.window)
        self.code_txt.place(x=80, y=20)

        self.name_txt = Entry(self.window)
        self.name_txt.place(x=80, y=50)

        self.unit_txt = Entry(self.window)
        self.unit_txt.place(x=80, y=80)

        self.count_txt = Entry(self.window)
        self.count_txt.place(x=80, y=110)

        self.price_txt = Entry(self.window)
        self.price_txt.place(x=80, y=140)
        """
        self.save_btn = Button(self.window, text="Save", command=self.save_person).place(x=100, y=180)
        self.edit_btn = Button(self.window, text="Edit").place(x=300, y=180)
        self.remove_btn = Button(self.window, text="Remove").place(x=400, y=180)
        self.cancel_btn = Button(self.window, text="Cancel").place(x=500, y=180)

        self.table = Treeview(self.window).place(x=300, y=20, height=140, width=275)
        """

        # Button(self.window, text="Save", command=self.save_person).place(x=100, y=180)
        Button(self.window, text="Save", command=self.save_stuff).place(x=100, y=180)
        Button(self.window, text="Edit").place(x=300, y=180)
        Button(self.window, text="Remove").place(x=400, y=180)
        Button(self.window, text="Cancel").place(x=500, y=180)
        Treeview(self.window).place(x=300, y=20, height=140, width=275)

        self.window.mainloop()

    def get_data(self):
        code = self.code_txt.get()
        name = self.name_txt.get()
        unit = self.unit_txt.get()
        count = self.count_txt.get()
        price = self.price_txt.get()

        # return code,name,unit,count,price
        return code, name, unit, count, price

    def save_stuff(self):
        # code,name,unit,count,price = self.get_data()
        code, name, unit, count, price = self.get_data()
        # s_control = StuffController(code,name,unit,count,price)
        s_control = StuffController(code, name, unit, count, price)
        s_control.add()
