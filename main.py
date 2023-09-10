class person:

    def __init__(self , name , age):
        self.name = name 
        self.age = age 

    def __str__(self):
        return f" my name is {self.name} my age is {self.age}"
    
    def is_adult(self):
        if self.age > 18 : 
            print("You have too much responsibilities")
        else:
            print("Lucky")


first_person = person("manal" , 22) # create an object 
print(first_person.name)
print(first_person.age)
first_person.is_adult()
print(first_person)