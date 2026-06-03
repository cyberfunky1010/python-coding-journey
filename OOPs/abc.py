class Customer():

    def __init__(self, name, age):
        
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"hi I'm {self.name} and I'm {self.age}")

c1 = Customer('aquib', 25)
c2 = Customer('muhammad', 28)
c3 = Customer('zakariah', 22)

l1 = [c1, c2, c3]  # list of objects 

for i in l1:       # call also loop over objects 
    i.intro()      # can also do prin(i.name, i.age) to merge in one, hence intro() 