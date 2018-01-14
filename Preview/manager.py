from person_start import Person

class Manager(Person):
    def __str__(self):
        return '%s => %s' % (self.__class__,self.name)
    def giveRaise(self, percent,bonus=0.1):
        Person.giveRaise(self,percent + bonus)

if __name__ == '__main__':
    tom = Manager(name = 'Tom Doe',age=50,pay=50000)
    print(tom)