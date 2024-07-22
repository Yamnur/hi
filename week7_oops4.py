class Actor:
    def __init__(self,  name):
        self.name = name
        
    def display(self):
        print(f"Name of the actor: {self.name}")

class director:
    def __init__(self, name_dir):
        self.name_dir = name_dir
        
    def display(self):
        print(f"Name of the director: {self.name_dir}")

class movie(Actor, director):
    def __init__(self, movie_name, name_dir, name_act):
        self.movie_name = movie_name
        director.__init__(self,name_dir)  # Initialize director's name via superclass
        Actor.__init__(self,name_act)  # Initialize actor's name via superclass
        
    def display(self):
        print("Name of the movie:", self.movie_name)
        super().display()   # Call display method of Actor superclass
        director.display(self)  # Call display method of director superclass

s = movie('abc', 'dfg', 'ghh')
s.display()

