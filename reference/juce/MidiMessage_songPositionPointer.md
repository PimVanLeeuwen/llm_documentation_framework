#### songPositionPointer()


 static MidiMessage MidiMessage::songPositionPointer ( int positionInMidiBeats ) staticnoexcept 
 

Creates a songpositionpointer message.The position is a number of midi beats from the start of the song, where 1 midi beat is 6 midi clocks, and there are 24 midi clocks in a quarternote. So there are 4 midi beats in a quarternote.See alsoisSongPositionPointer, getSongPositionPointerMidiBeat