#### getSysExData()


 const uint8 \* MidiMessage::getSysExData ( ) const noexcept 
 

Returns a pointer to the sysex data inside the message.If this event isn't a sysex event, it'll return 0.See alsogetSysExDataSize