#### getTimeStamp()


 double MidiMessage::getTimeStamp ( ) const noexcept 
 

Returns the timestamp associated with this message.The exact meaning of this time and its units will vary, as messages are used in a variety of different contexts.If you're getting the message from a midi file, this could be a time in seconds, or a number of ticks see MidiFile::convertTimestampTicksToSeconds().If the message is being used in a MidiBuffer, it might indicate the number of audio samples from the start of the buffer.If the message was created by a MidiInput, see MidiInputCallback::handleIncomingMidiMessage() for details of the way that it initialises this value.See alsosetTimeStamp, addToTimeStamp