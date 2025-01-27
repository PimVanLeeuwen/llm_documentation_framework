#### addEvent() [2/2]


 MidiEventHolder \* MidiMessageSequence::addEvent ( MidiMessage && newMessage, 
 
 double timeAdjustment = 0 ) 

Inserts a midi message into the sequence.The index at which the new message gets inserted will depend on its timestamp, because the sequence is kept sorted.Remember to call updateMatchedPairs() after adding noteon events.Parameters

 newMessage the new message to add (an internal copy will be made) 
 
 timeAdjustment an optional value to add to the timestamp of the message that will be inserted 



See alsoupdateMatchedPairs