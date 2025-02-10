#### updateMatchedPairs()


 void MidiMessageSequence::updateMatchedPairs ( ) noexcept 
 

Makes sure all the noteon and noteoff pairs are uptodate.Call this after reordering messages or deleting/adding messages, and it will scan the list and make sure all the noteoffs in the MidiEventHolder structures are pointing at the correct ones.