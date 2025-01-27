#### getChannel()


 int MidiMessage::getChannel ( ) const noexcept 
 

Returns the midi channel associated with the message.Returnsa value 1 to 16 if the message has a channel, or 0 if it hasn't (e.g. if it's a sysex) 
See alsoisForChannel, setChannel