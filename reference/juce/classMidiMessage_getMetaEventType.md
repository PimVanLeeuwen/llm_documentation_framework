#### getMetaEventType()


 int MidiMessage::getMetaEventType ( ) const noexcept 
 

Returns a metaevent's type number.If the message isn't a metaevent, this will return 1.See alsoisMetaEvent, isTrackMetaEvent, isEndOfTrackMetaEvent, isTextMetaEvent, isTrackNameEvent, isTempoMetaEvent, isTimeSignatureMetaEvent, isKeySignatureMetaEvent, isMidiChannelMetaEvent