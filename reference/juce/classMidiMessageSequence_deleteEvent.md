#### deleteEvent()


 void MidiMessageSequence::deleteEvent ( int index, 
 
 bool deleteMatchingNoteUp ) 

Deletes one of the events in the sequence.Remember to call updateMatchedPairs() after removing events.Parameters

 index the index of the event to delete 
 
 deleteMatchingNoteUp whether to also remove the matching noteoff if the event you're removing is a noteon