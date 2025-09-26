class Person:
    def __init__(self, name, family, birth_date, role, code=0):
        print("Person Entity")
        self.code = code
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.role = role

    def __str__(self):
        return f"{self.code} - {self.name} {self.family} - {self.birth_date} - {self.role}"
