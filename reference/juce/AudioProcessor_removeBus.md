#### removeBus()


 bool AudioProcessor::removeBus ( bool isInput ) 
 

Dynamically remove the latest added bus.Request the removal of the last bus from the audio processor. If the audio processor does not support removing buses then this method will return false.Most audio processors will not allow you to dynamically add/remove audio buses and will return false.The default implementation will return false.This method will invoke the canApplyBusCountChange callback to probe if a bus can currently be removed and, if yes, will go ahead and remove it.See alsoaddBus, canRemoveBus