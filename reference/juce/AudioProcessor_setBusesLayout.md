#### setBusesLayout()


 bool AudioProcessor::setBusesLayout ( const BusesLayout & ) 
 

Set the channel layouts of this audio processor.If the layout is not supported by this audio processor then this method will return false. You can use the checkBusesLayoutSupported and getNextBestLayout methods to probe which layouts this audio processor supports.