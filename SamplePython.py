class Dog():
    def __init__(self,breed,name,spot):
        self.breed = breed
        self.name = name
        self.spot = spot

    def my_dog(self):
        if self.spot:
            print(f'My dog is of {self.breed} breed and we call him {self.name} also he has few spots!!!')
        else:
            print(f'My dog is of {self.breed} breed and we call him {self.name} also he has no spots!!!')

# creating instance of the class

my_obj = Dog('German Shepeard','Cindrella',True)

my_obj.my_dog()