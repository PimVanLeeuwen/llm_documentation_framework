#### deviceRemoved()


 virtual void midi\_ci::DeviceListener::deviceRemoved ( MUID x ) virtual 
 

Called to indicate that a device's MUID was invalidated.If you were previously storing your own information about this device, you should forget that information here.