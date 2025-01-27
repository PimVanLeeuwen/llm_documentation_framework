#### copyState()


 ValueTree AudioProcessorValueTreeState::copyState ( ) 
 

Returns a copy of the state value tree.The AudioProcessorValueTreeState's ValueTree is updated internally on the message thread, but there may be cases when you may want to access the state from a different thread (getStateInformation is a good example). This method flushes all pending audio parameter value updates and returns a copy of the state in a thread safe way.Note: This method uses locks to synchronise thread access, so whilst it is threadsafe, it is not realtimesafe. Do not call this method from within your audio processing code!