from tkinter import *
from backend import smartplug
from backend import smartdoor
from backend import smartHome

mainWin = Tk()
Homesmart = smartHome()

def setupHome():
    
        Smartdoor1 = smartdoor(False ,True) 
        Smartdoor2 = smartdoor(False ,True) 
        Smartplug1 = smartplug(False,0)
        Smartplug2 = smartplug(False,0)
        Smartdoor3 = smartdoor(False ,True) 

        Homesmart.addDevice(Smartdoor1)
        Homesmart.addDevice(Smartdoor2)
        Homesmart.addDevice(Smartplug1)
        Homesmart.addDevice(Smartplug2)
        Homesmart.addDevice(Smartdoor3)

        device_totalnum= len(Homesmart.getDevices())
        mainWin.title('smarthome')
        
        mainWin.geometry('550x350')
        count = 0
       
        mainWin.columnconfigure(index=0, weight=3)
        mainWin.columnconfigure(index=1, weight=1)
        outputText = Label(mainWin,height=1, width=12, 
                            font=('Times', 20, 'bold'),text='Smart Home')
        outputText.grid(row=0, column=0, columnspan=2)
           
        for deviceIndex in range(device_totalnum):
            
            device = Homesmart.getDeviceAt(deviceIndex)   

            deviceTxt=Text(mainWin, height=2, width=50)
            deviceTxt.insert("1.0", str(device))
            deviceTxt.grid(row=deviceIndex + 3, column=0, padx=10, pady=5)
            
            def on():
                 Homesmart.turnOnAll() 
                 display1(i=deviceIndex)
            Turn_all_on = Button(mainWin, text="Turn all on", command=on)
            Turn_all_on.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
            def off():
                 Homesmart.turnOffAll() 
                 display1(i=deviceIndex)    
            Turn_all_off = Button(mainWin, text="Turn all off", command=off)
            Turn_all_off.grid(row=2, column=0, padx=80, pady=10, sticky="w")
         
            def onoff(i=deviceIndex):
               
                nonlocal count
                count+=1

                if count == 1:     
            
                    Homesmart.toggleSwitch(i)        
                    display1(i)
                    count=2
                else:
                   
                    Homesmart.toggleSwitch(i)
                    display1(i)
                    count = 0
                        
            configBtn = Button(mainWin, text="Toogle this", command=onoff)
            configBtn.grid(row=deviceIndex+ 3, column=1, padx=5, pady=5)
                  
        mainWin.mainloop()

def display1(i):
      
        device_totalnum= len(Homesmart.getDevices())
    
        for i in range(device_totalnum):
            
                device = Homesmart.getDeviceAt(i)
                deviceTxt=Text(mainWin, height=2, width=50)
                deviceTxt.insert("1.0", str(device))
                deviceTxt.grid(row=i + 3, column=0, padx=10, pady=5)
    
def main():   
    setupHome()

main()    
   

    
       