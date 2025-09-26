
from anbar.model.da.PersonDA import PersonDA
from anbar.model.entity.Person import Person

# from model.da.PersonDA import PersonDA
# from model.entity.Person import Person


class PersonController:
    def __init__(self, code, name, family, birth_date, role):
        print("Person Controller")
        if int(code) > 0 and name != "" and family != "" and birth_date != "" and role != 0:
            self.person = Person(code, name, family, birth_date, role)
        else:
            self.person = None

    def add(self):
        # if self.person != None:
        if self.person is not None:
            p_da = PersonDA()
            p_da.add(self.person)


    def edit(self):
        if self.person is not None:
            p_da = PersonDA()
            p_da.edit(self.person)

