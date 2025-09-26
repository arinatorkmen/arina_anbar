from tkinter import *
from tkinter.ttk import *

from anbar.controller.PersonController import PersonController
# from controller.PersonController import PersonController


class PersonUI:
    def __init__(self):
        print("PersonView")
        labels = ['Code', 'Name', 'Family', 'Birth Date', 'Role']

        self.window = Tk()
        self.window.title("Person")
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

        self.family_txt = Entry(self.window)
        self.family_txt.place(x=80, y=80)

        self.birth_date_txt = Entry(self.window)
        self.birth_date_txt.place(x=80, y=110)

        self.role_cmb = Combobox(self.window)
        self.role_cmb['values'] = ["تحویل دهنده", "تحویل گیرنده"]
        self.role_cmb.current(1)
        self.role_cmb.place(x=80, y=140, width=125)

        """
        self.save_btn = Button(self.window, text="Save", command=self.save_person).place(x=100, y=180)
        self.edit_btn = Button(self.window, text="Edit").place(x=300, y=180)
        self.remove_btn = Button(self.window, text="Remove").place(x=400, y=180)
        self.cancel_btn = Button(self.window, text="Cancel").place(x=500, y=180)

        self.table = Treeview(self.window).place(x=300, y=20, height=140, width=275)
        """

        Button(self.window, text="Save", command=self.save_person).place(x=100, y=180)
        Button(self.window, text="Edit").place(x=300, y=180)
        Button(self.window, text="Remove").place(x=400, y=180)
        Button(self.window, text="Cancel").place(x=500, y=180)
        Treeview(self.window).place(x=300, y=20, height=140, width=275)

        self.window.mainloop()

    def get_data(self):
        code = self.code_txt.get()
        name = self.name_txt.get()
        family = self.family_txt.get()
        birth_date = self.birth_date_txt.get()
        if self.role_cmb.get() == "تحویل دهنده":
            role = 1
        elif self.role_cmb.get() == "تحویل گیرنده":
            role = -1
        else:
            role = 0
        # return code,name,family,birth_date,role
        return code, name, family, birth_date, role

    def save_person(self):
        # code,name,family,birth_date,role = self.get_data()
        code, name, family, birth_date, role = self.get_data()
        # p_control = PersonController(code,name,family,birth_date,role)
        p_control = PersonController(code, name, family, birth_date, role)
        p_control.add()

    # def edit_person(self):
    #     self.get_data()
    #     p_control = PersonController()
    #     p_control.edit()
