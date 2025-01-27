#### noteOffObject


 MidiEventHolder\* MidiMessageSequence::MidiEventHolder::noteOffObject = nullptr 
 

The matching noteoff event (if this is a noteon event).If this isn't a noteon, this pointer will be nullptr.Use the MidiMessageSequence::updateMatchedPairs() method to keep these noteoffs uptodate after events have been moved around in the sequence or deleted.