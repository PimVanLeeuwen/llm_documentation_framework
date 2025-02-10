#### replaceState()


 void AudioProcessorValueTreeState::replaceState ( const ValueTree & newState ) 
 

Replaces the state value tree.The AudioProcessorValueTreeState's ValueTree is updated internally on the message thread, but there may be cases when you may want to modify the state from a different thread (setStateInformation is a good example). This method allows you to replace the state in a thread safe way.Note: This method uses locks to synchronise thread access, so whilst it is threadsafe, it is not realtimesafe. Do not call this method from within your audio processing code!

Member Data Documentation