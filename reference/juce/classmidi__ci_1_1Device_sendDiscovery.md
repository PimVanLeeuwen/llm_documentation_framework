#### sendDiscovery()


 void midi\_ci::Device::sendDiscovery ( ) 
 

Sends an inquiry message.You can use DeviceListener::deviceAdded to be notified when new devices are discovered.This will clear the internal cache of discovered devices, and repopulate it as discovery response messages are received.