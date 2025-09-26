from anbar.model.da.StuffDA import StuffDA
from anbar.model.entity.Stuff import Stuff


class StuffController:
    def __init__(self, code, name, unit, count, price):
        # print("Person Controller")
        print("Stuff Controller")
        if int(code) > 0 and name != "" and unit != "" and int(count) > 0 and int(price) > 0:
            self.stuff = Stuff(code, name, unit, count, price)
        else:
            self.stuff = None

    def add(self):
        if self.stuff is not None:
            s_da = StuffDA()
            s_da.add(self.stuff)

    def edit(self):
        if self.stuff is not None:
            p_da = StuffDA()
            p_da.edit(self.stuff)

