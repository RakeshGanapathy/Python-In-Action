class Student:
    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram

    def config(self):
        print("Config is {} ,{}".format(self.processor, self.ram))


perf1 = Student("ryzen", 3)
perf1.config()
perf2 = Student('i3', 4)
perf2.config()
