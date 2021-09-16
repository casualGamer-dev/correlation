class cars (object):
    def __init__ (self):
        self.number= ""
        self.color = ""
        self.brand= ""
        self.model = ""
        self.owner= ""
        self.list =[]


    def setNumber(self):
        self.number = int(input("enter your phone number  "))
        self.list.append(self.number)
    def setBrand(self):
        self.brand = input("enter the brand  ")
        self.list.append(self.brand)
    def setColor(self):
        self.color  = input("enter the color  ")
        self.list.append(self.color)
    def setModel(self):
        self.model = input("enter the model  ")
        self.list.append(self.model)
    def Owner(self):
        self.owner = input("enter your name  ")
        self.list.append(self.owner)
    def CreateList(self):
         return self.list
        
sellerList=cars()
sellerList.Owner()
sellerList.setNumber()
sellerList.setBrand()
sellerList.setModel()
sellerList.setColor()
print(sellerList.CreateList())
    