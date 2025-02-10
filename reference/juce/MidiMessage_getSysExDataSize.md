#### getSysExDataSize()


 int MidiMessage::getSysExDataSize ( ) const noexcept 
 

Returns the size of the sysex data.This value excludes the 0xf0 header byte and the 0xf7 at the end.See alsogetSysExData