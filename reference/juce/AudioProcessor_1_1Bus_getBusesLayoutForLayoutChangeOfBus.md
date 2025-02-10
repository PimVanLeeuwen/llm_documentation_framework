#### getBusesLayoutForLayoutChangeOfBus()


 BusesLayout AudioProcessor::Bus::getBusesLayoutForLayoutChangeOfBus ( const AudioChannelSet & set ) const 
 

Returns the resulting layouts of all buses after changing the layout of this bus.Changing an individual layout of a bus may also change the layout of all the other buses. This method returns what the layouts of all the buses of the audio processor would be, if you were to change the layout of this bus to the given layout. If there is no way to support the given layout then this method will return the next best layout.