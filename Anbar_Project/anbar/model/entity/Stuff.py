class Stuff:
    def __init__(self, name, unit, count, price, code=0):
        print("Person Entity")
        self.code = code
        self.name = name
        self.unit = unit
        self.count = count
        self.price = price

    def __str__(self):
        return f"{self.code} - {self.name} {self.unit} - {self.count} - {self.price}"
