# initialize attributes(instance variables)
# constructor
# initalizing instance variable (duty of constructor)
# constructor in python is __init__

class Movie:

    title:str

    rating:int

    run_time:int

    director:str

    genre:str

    def set_movie(self,title,rating,run_time,director,genre):

        self.title=title

        self.rating=rating

        self.run_time=run_time

        self.director=director

        self.genre=genre


    def display(self):

        print(self.title,self.rating,self.director)


movie_instance=Movie()

movie_instance.set_movie("ARM",4.5,150,"jithin lal","action")

movie_instance.display()