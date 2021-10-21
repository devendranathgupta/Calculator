class calculator: #forming a class as calculattor 
    def __init__(self,num) -> None: #defining a constructor
        self.num = num

    def square(self): #for the square root finding fucntion is defined 
        print(f"The value of the square is : {self.num} is {self.num**2}")

    def squareRoot(self): #for the square root finding function is defined 
        print(f"The value of the square is {self.num} is {self.num**0.5}")

    def cube(self): #for the cube root  finding function is defined
        print(f"The value of the square is :  {self.num} is {self.num**3}")

a = calculator((int(input("Enter the number :")))) #iving the value of the function which you want to calcullate 
a.square()
a.cube()
a.squareRoot()   