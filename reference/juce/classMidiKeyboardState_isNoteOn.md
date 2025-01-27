#### isNoteOn()


 bool MidiKeyboardState::isNoteOn ( int midiChannel, int midiNoteNumber ) const noexcept 
 

Returns true if the given midi key is currently held down for the given midi channel.The channel number must be between 1 and 16. If you want to see if any notes are on for a range of channels, use the isNoteOnForChannels() method.