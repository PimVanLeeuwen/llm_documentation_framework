#### findMidiChannelForNewNote()


 int MPEChannelAssigner::findMidiChannelForNewNote ( int noteNumber ) noexcept 
 

This method will use a set of rules recommended in the MPE specification to determine which member channel the specified MIDI note should be assigned to and will return this channel number.The rules have the following precedence:find a free channel on which the last note played was the same as the one specifiedfind the next free channel in roundrobin assignmentfind the channel number that is currently playing the closest note (but not the same)Parameters

 noteNumber the MIDI note number to be assigned to a channel 
 



Returnsthe zone's member channel that this note should be assigned to