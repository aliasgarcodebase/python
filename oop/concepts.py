class Person:
    name = "Aliasgar Vanak"
    occupation = "Software Developer"
    def myInfo(self):
        print(self.name +" is a "+self.occupation)
        #print(self.name)

a = Person()
a.myInfo()

b = Person()
b.name = "Siddharth Kar"
b.occupation = "Software Engineer"
b.myInfo()
