

class SuperHero:

    def __init__(self,name,suite):

        self.name=name

        self.suite=suite

    def __str__(self):

        return self.name
    
class SpiderMan(SuperHero):

    def __init__(self, name, suite):
        super().__init__(name, suite,)

    def super_power(self):

        print("spider sense","web shooting","sticky hands")

class MinnalMurali("minnalmurali","minnalmurali suite"):

    print("running","jumping","reflex")

MinnalMurali_instance=MinnalMurali("minnalmurali","minnalmurali suite")

print(MinnalMurali_instance)