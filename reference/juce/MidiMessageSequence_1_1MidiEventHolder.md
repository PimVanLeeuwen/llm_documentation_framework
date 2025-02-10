Structure used to hold midi events in the sequence.These structures act as 'handles' on the events as they are moved about in the list, and make it quick to find the matching noteoffs for noteon events.See alsoMidiMessageSequence::getEventPointer 

Member Data Documentation


◆ message


 MidiMessage MidiMessageSequence::MidiEventHolder::message 
 

The message itself, whose timestamp is used to specify the event's time.

◆ noteOffObject


 MidiEventHolder\* MidiMessageSequence::MidiEventHolder::noteOffObject = nullptr 
 

The matching noteoff event (if this is a noteon event).If this isn't a noteon, this pointer will be nullptr.Use the MidiMessageSequence::updateMatchedPairs() method to keep these noteoffs uptodate after events have been moved around in the sequence or deleted.