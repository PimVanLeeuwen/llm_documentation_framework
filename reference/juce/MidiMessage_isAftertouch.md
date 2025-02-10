#### isAftertouch()


 bool MidiMessage::isAftertouch ( ) const noexcept 
 

Returns true if the message is an aftertouch event.For aftertouch events, use the getNoteNumber() method to find out the key that it applies to, and getAfterTouchValue() to find out the amount. Use getChannel() to find out the channel.See alsogetAftertouchValue, getNoteNumber