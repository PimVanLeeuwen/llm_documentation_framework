#### addSequence() [2/2]


 void MidiMessageSequence::addSequence ( const MidiMessageSequence & other, 
 
 double timeAdjustmentDelta ) 

Merges another sequence into this one.Remember to call updateMatchedPairs() after using this method.Parameters

 other the sequence to add from 
 
 timeAdjustmentDelta an amount to add to the timestamps of the midi events as they are read from the other sequence