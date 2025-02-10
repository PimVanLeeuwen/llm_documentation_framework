#### isBusesLayoutSupported()


 virtual bool AudioProcessor::isBusesLayoutSupported ( const BusesLayout & ) const protectedvirtual 
 

Callback to query if the AudioProcessor supports a specific layout.This callback is called when the host probes the supported bus layouts via the checkBusesLayoutSupported method. You should override this callback if you would like to limit the layouts that your AudioProcessor supports. The default implementation will accept any layout. JUCE does basic sanity checks so that the provided layouts parameter will have the same number of buses as your AudioProcessor.See alsocheckBusesLayoutSupported