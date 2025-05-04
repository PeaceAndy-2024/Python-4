#Question 1
class Smartphone:
    colour= "sea green"
    Model= "Samsung"
    # Method to display 
    def switchon(self):
         print("the phone is switching on")
    def  restart(self):
         print("the phone is restarting")

    
    class Smartphone:
        #constructor to initialize the object
        def __init__(self,model,colour):
            self.model= model #instance variable for model
            self.colour= colour # instance variable for colour
    
    smartphoneDetails  = Smartphone("Samsung","sea green")   #create an instance of the smartphone class 
    
    print(smartphoneDetails.colour) # Access the colour attribute 
    
    class Smartphone:
        #inheritance to initialize the object 
        def __init__(self, sidebuttons):
            self.sidebuttons= sidebuttons 
    
    
    smartphone= Smartphone(2)
    print(smartphone.sidebuttons)# output:2
    
    class SecretStash:
        #encapsulation to initialize the object 
        def __init__(self):
            self.__earpods=2 #private attribute 
            
        def take_earpod(self):
             if self.__earpods>0:
                self.__earpods-=1 
                print ("one earpod taken!")
             else:
                print("no earpods left")
        
    stash=SecretStash()
    stash.take_earpod()
    
my_smartphone= Smartphone()#create an instance of the class Smartphone 
my_smartphone.switchon() #call the switch on method 
my_smartphone.restart() #call the restart method 
    #print(my_smartphone.colour) #access the colour attribute



#Activity two
     #Polymorphism 
     
    class  Goat:
         def speak(self):
             return "baaah!"
    
    class  Cow:
        def speak(self):
            return"mooh"
            
   #polymorphism in action 
for animal in [Goat(), Cow()]:
       print(animal.speak())
    
    
    
    
    
    
    
    
    
