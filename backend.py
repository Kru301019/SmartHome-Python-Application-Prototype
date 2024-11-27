class smartplug:
   
    def __init__(self,switchedon,consumptionRate):
        self.switchedon = switchedon
        self.consumptionRate = consumptionRate

    def toggle_Switch(self):
       
        if self.switchedon == False:
         self.switchedon = True
        else:
         self.switchedon = False
         
    def toggle_Switch_on(self):
        self.switchedon=True

    def toggle_Switch_off(self):
        self.switchedon = False
         
    def getswichedon(self):
        return self.switchedon
        
    def getconsumptionRate(self):
        return self.consumptionRate

    def setconsumptionRate(self,newrate):
        self.newrate  = newrate
        self.consumptionRate+=self.newrate 

    def __str__(self):
       
        output = "consumptionrate is is:{}".format(self.consumptionRate)
        
        if self.switchedon:
            output += " and swicth is:ON".format(self.switchedon)
        else:
            output+=" and swich is:OFF".format(self.switchedon)
        
        return output
            
def testsmartplug():
   
    Smartplug = smartplug(True,0)
   # Smartplug.toggle_Switch()
    print(Smartplug.getswichedon())
    print(Smartplug.getconsumptionRate())
    print(Smartplug.setconsumptionRate(60))
    print(Smartplug.getconsumptionRate())
    print(Smartplug)
    
    
    if Smartplug.getswichedon() == True:
        print('hello')
         
    
testsmartplug()

class smartdoor():
    def __init__(self, switchedOn, locked):
        
        self.switchedOn = switchedOn
        self.locked = locked
        
    def toggle_Switch(self):
        if self.switchedOn==True:
         self.switchedOn = False
        else:
            self.switchedOn = True
        
    def toggle_Switch_on(self):
        self.switchedOn=True

    def toggle_Switch_off(self):
        self.switchedOn = False
   
    def get_switchedOn(self):
        return self.switchedOn
    
    def get_locked(self):
        return self.locked
    
    def set_locked(self):
        self.locked = False
        
    def __str__(self):
        
        if self.switchedOn:
            output = 'The swich is on '
            
            if self.locked:
                output+='and The door is locked'
            
            else:
                output+='and The door is unlocked'    
        
        else:
            
            output = 'The swich is off '
            
            if self.locked:
                output+='and The door is locked'
            
            else:
                output+='and The door is unlocked' 
            
        return output        
            
def testsmartdoor():
   
    Smartdoor = smartdoor(True ,True)   
    Smartdoor.toggle_Switch()
    print(Smartdoor.get_switchedOn())
    print(Smartdoor.get_locked())
    Smartdoor.set_locked()   
    print(Smartdoor.get_locked())
    print(Smartdoor)

class smartHome():
    def __init__(self):
        self.devices = []
        
    def getDevices(self):
        return self.devices
    
    def getDeviceAt(self,index):
       return  self.devices[index]
         
    def addDevice(self,device):
         self.devices.append(device)
    
    def toggleSwitch(self,index): 
        self.devices[index].toggle_Switch()

    def turnOnAll(self):
      
        for i in range (len(self.devices)):
            self.devices[i].toggle_Switch_on()

    def turnOffAll(self):
        for i in range(len(self.devices)):
            self.devices[i].toggle_Switch_off()

    def __str__(self) :
    
        out=''
        for device in self.devices:
            
            out=out+'{}\n'.format(device)     
        return out

def test_smarthome():
    
      Smarthome = smartHome()      
      plug1 = smartplug(False,0)
      plug2 = smartplug(False,0)
      Smartdoor1 = smartdoor(False ,True)  
      plug2.toggle_Switch()
      plug2.setconsumptionRate(45) 
      Smartdoor1.set_locked()
    
      Smarthome.addDevice(plug1)
      Smarthome.addDevice(plug2)
      Smarthome.addDevice(Smartdoor1)
    
      print(Smarthome)
     
      lenth = len(Smarthome.getDevices())

    #   for i in range(lenth):
    #      Smarthome.toggleSwitch(i)
    #   print(Smarthome)   


      
    