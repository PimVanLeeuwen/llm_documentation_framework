#### canRemoveBus()


 virtual bool AudioProcessor::canRemoveBus ( bool isInput ) const virtual 
 

Callback to query if the last bus can currently be removed.This callback probes if the last bus can currently be removed. You should override this callback if you want to support dynamically adding/removing buses by the host. This is useful for mixer audio processors.If you return true in this callback then the AudioProcessor will go ahead and delete the bus.The default implementation will always return false.