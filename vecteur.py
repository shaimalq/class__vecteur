class vecteur ():
    def __init__(self , x , y , z ):
        self.__x= x  
        self.__y = y
        self.__z = z 

    def getx(self):
        return self.__x
    
    def setx (self , x):
      self.__x = x
     
    def gety (self) :
        return self.y
    

    def sety (self , y):
      self.__y = y
   
      
    def getz(self):
        return self.__z
   
    def setz (self , z):
      self.__z = z
   


    def info (self):
      print (f"x : {self.__x}\ny:{self.__y}\nz:{self.__z}\n{self.__x.getx()}\n {self.__y.gety()}\n{self.__z.getz()}\n{self.__z.getz()}")

p1 =vecteur ( 2 , 4 ,8)
 
p1.info()
   
pass