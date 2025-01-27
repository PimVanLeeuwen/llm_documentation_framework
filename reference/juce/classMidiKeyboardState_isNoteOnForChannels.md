#### isNoteOnForChannels()


 bool MidiKeyboardState::isNoteOnForChannels ( int midiChannelMask, int midiNoteNumber ) const noexcept 
 

Returns true if the given midi key is currently held down on any of a set of midi channels.The channel mask has a bit set for each midi channel you want to test for bit 0 = midi channel 1, bit 1 = midi channel 2, etc.If a note is on for at least one of the specified channels, this returns true.