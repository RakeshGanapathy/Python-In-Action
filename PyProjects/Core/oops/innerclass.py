
class Teacher:
    school = "KV"

    def __init__(self, name, id, staff):
        self.name = name
        self.id = id
        self.staff = staff

    def show(self):
        print(self.name, self.id)

    def __str__(self) -> str:
        return "the info are {} , {} ".format(self.id, self.name)

    class Staff:
        def __init__(self, hostel, resp):
            self.hostel = hostel
            self.resp = resp

        def show(self):
            print(self.hostel, self.resp)


staff1 = Teacher.Staff("TRS","incharge")
person = Teacher("rakesh", 23, staff1)
divya = Teacher("divya", 23 ,staff1)
print(person)
print(id(person))
print(person)
print(id(divya))
print(divya)
