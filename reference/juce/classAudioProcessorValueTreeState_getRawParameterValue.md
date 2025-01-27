#### getRawParameterValue()


 std::atomic< float > \* AudioProcessorValueTreeState::getRawParameterValue ( StringRef parameterID ) const noexcept 
 

Returns a pointer to a floating point representation of a particular parameter which a realtime process can read to find out its current value.Note that calling this method from within AudioProcessorValueTreeState::Listener::parameterChanged() is not guaranteed to return an uptodate value for the parameter.