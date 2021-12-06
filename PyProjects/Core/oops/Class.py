


class Person:
    personName =""

    def config(self):
        print("Hi Dude")

name = "rakesh"
id = 23
comp = Person()
compute = Person.config(comp);
print(type(name))
print(type(id))
print(type(compute))

comp.config()
