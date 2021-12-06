class Teacher:
    school = "KV"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return "the info are {} , {} ".format(self.id, self.name)


person = Teacher("rakesh", 23)
divya = Teacher("divya", 23)
print(person)
print(id(person))
print(person)
print(id(divya))
print(divya)
