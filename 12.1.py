class animal:
    def sound(self):
         pass
class cat(animal):
    def sound(self):
        print("memo")
class Dog(animal):
    def sound(self):
        print("woof")
def make_sound(animal):
     animal.sound()
cat=cat()
dog=Dog()
make_sound(cat)
make_sound(dog)
