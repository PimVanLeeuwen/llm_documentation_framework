#### setBusesLayoutWithoutEnabling()


 bool AudioProcessor::setBusesLayoutWithoutEnabling ( const BusesLayout & ) 
 

Set the channel layouts of this audio processor without changing the enablement state of the buses.If the layout is not supported by this audio processor then this method will return false. You can use the checkBusesLayoutSupported methods to probe which layouts this audio processor supports.