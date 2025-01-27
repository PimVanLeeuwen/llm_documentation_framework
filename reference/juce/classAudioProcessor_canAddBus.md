#### canAddBus()


 virtual bool AudioProcessor::canAddBus ( bool isInput ) const virtual 
 

Callback to query if a bus can currently be added.This callback probes if a bus can currently be added. You should override this callback if you want to support dynamically adding/removing buses by the host. This is useful for mixer audio processors.The default implementation will always return false.See alsoaddBus