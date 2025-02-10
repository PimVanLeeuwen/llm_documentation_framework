#### isMetaEvent()


 bool MidiMessage::isMetaEvent ( ) const noexcept 
 

Returns true if this event is a metaevent.Metaevents are things like tempo changes, track names, etc.See alsogetMetaEventType, isTrackMetaEvent, isEndOfTrackMetaEvent, isTextMetaEvent, isTrackNameEvent, isTempoMetaEvent, isTimeSignatureMetaEvent, isKeySignatureMetaEvent, isMidiChannelMetaEvent