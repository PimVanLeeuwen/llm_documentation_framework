#### getFullFrameParameters()


 void MidiMessage::getFullFrameParameters ( int & hours, int & minutes, int & seconds, int & frames, SmpteTimecodeType & timecodeType ) const noexcept 
 

Extracts the timecode information from a fullframe midi timecode message.You should only call this on messages where you've used isFullFrame() to check that they're the right kind.