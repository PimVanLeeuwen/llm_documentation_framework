#### getTimeOfMatchingKeyUp()


 double MidiMessageSequence::getTimeOfMatchingKeyUp ( int index ) const noexcept 
 

Returns the time of the noteup that matches the noteon at this index.If the event at this index isn't a noteon, it'll just return 0.See alsoMidiMessageSequence::MidiEventHolder::noteOffObject