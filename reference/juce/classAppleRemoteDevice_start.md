#### start()


 bool AppleRemoteDevice::start ( bool inExclusiveMode ) 
 

Starts the device running and responding to events.Returns true if it managed to open the device.Parameters

 inExclusiveMode if true, the remote will be grabbed exclusively for this app, and will not be available to any other part of the system. If false, it will be shared with other apps. 
 



See alsostop