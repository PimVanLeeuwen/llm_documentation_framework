#### findMidiChannelForExistingNote()


 int MPEChannelAssigner::findMidiChannelForExistingNote ( int initialNoteOnNumber ) noexcept 
 

If a note has been added using findMidiChannelForNewNote() this will return the channel to which it was assigned, otherwise it will return 1.