#### addBus()


 bool AudioProcessor::addBus ( bool isInput ) 
 

Dynamically request an additional bus.Request an additional bus from the audio processor. If the audio processor does not support adding additional buses then this method will return false.Most audio processors will not allow you to dynamically add/remove audio buses and will return false.This method will invoke the canApplyBusCountChange callback to probe if a bus can be added and, if yes, will use the supplied bus properties of the canApplyBusCountChange callback to create a new bus.See alsocanApplyBusCountChange, removeBus