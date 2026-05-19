# create my own data type. this is used to perform fraction calculation and print in fraction format.

class Fraction:
    
    #constructor
    def __init__(self,n,d):
        
        self.num = n    # created variable num and put value of n
        self.den = d    # created variable den and put value of d
         
         #at this point i've NOT defined how my fraction class works 
    def __str__(self):           # this runs when using print(x), used to define a human-readable string representation of an object
          return "{}/{}".format(self.num, self.den)            
    
    def __add__(self, other):  #self takes left side of + while other takes right side of +.
         temp_num = self.num * other.den + other.num * self.den
         temp_den = self.den * other.den

         return "{}/{}".format(temp_num,temp_den)
    
    def __sub__(self, other):  
         temp_num = self.num * other.den - other.num * self.den
         temp_den = self.den * other.den

         return "{}/{}".format(temp_num,temp_den)
    
    def __mul__(self, other):  
         temp_num = self.num * other.num
         temp_den = self.den * other.den

         return "{}/{}".format(temp_num,temp_den)
    
    def __truediv__(self, other):  
         temp_num = self.num * other.den
         temp_den = self.den * other.num

         return "{}/{}".format(temp_num,temp_den)
    