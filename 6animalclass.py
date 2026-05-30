class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "animal sound"
class dog(animal):
    def speak(self):
        return "bark"
class cat(animal):
    def speak(self):
        return "meow"
dog=dog("tommy")
cat=cat("kitty")
print( f"{dog.name} says {dog.speak()}")
print( f"{cat.name} says {cat.speak()}")