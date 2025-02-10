#### addEvents()


 void MidiBuffer::addEvents ( const MidiBuffer & otherBuffer, 
 
 int startSample, 
 int numSamples, 
 int sampleDeltaToAdd ) 

Adds some events from another buffer to this one.Parameters

 otherBuffer the buffer containing the events you want to add 
 
 startSample the lowest sample number in the source buffer for which events should be added. Any source events whose timestamp is less than this will be ignored 
 numSamples the valid range of samples from the source buffer for which events should be added i.e. events in the source buffer whose timestamp is greater than or equal to (startSample + numSamples) will be ignored. If this value is less than 0, all events after startSample will be taken. 
 sampleDeltaToAdd a value which will be added to the source timestamps of the events that are added to this buffer