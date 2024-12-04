
class Animal:

    specias:str

    name:str


    def __init__(self,name,speacias):

        self.name=name

        self.specias=speacias


    def __str__(self):

        return self.name
    
class Lion(Animal):

    def __init__(self, name, speacias):
        super().__init__(name, speacias)


    def sound(self):

        print("roar")


lion_instance=Lion("lion","catnivorous")

print(lion_instance)

print(lion_instance.sound())


