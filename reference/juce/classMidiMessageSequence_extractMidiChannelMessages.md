#### extractMidiChannelMessages()


 void MidiMessageSequence::extractMidiChannelMessages ( int channelNumberToExtract, 
 
 MidiMessageSequence & destSequence, 
 bool alsoIncludeMetaEvents ) const 

Copies all the messages for a particular midi channel to another sequence.Parameters

 channelNumberToExtract the midi channel to look for, in the range 1 to 16 
 
 destSequence the sequence that the chosen events should be copied to 
 alsoIncludeMetaEvents if true, any metaevents (which don't apply to a specific channel) will also be copied across. 



See alsoextractSysExMessages