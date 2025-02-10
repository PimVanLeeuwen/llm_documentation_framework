#### getIndexOfMatchingKeyUp()


 int MidiMessageSequence::getIndexOfMatchingKeyUp ( int index ) const noexcept 
 

Returns the index of the noteup that matches the noteon at this index.If the event at this index isn't a noteon, it'll just return 1.See alsoMidiMessageSequence::MidiEventHolder::noteOffObject