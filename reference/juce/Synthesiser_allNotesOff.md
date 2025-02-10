#### allNotesOff()


 virtual void Synthesiser::allNotesOff ( int midiChannel, bool allowTailOff ) virtual 
 

Turns off all notes.This will turn off any voices that are playing a sound on the given midi channel.If midiChannel is 0 or less, then all voices will be turned off, regardless of which channel they're playing. Otherwise it represents a valid midi channel, from 1 to 16 inclusive.If allowTailOff is true, the voices will be allowed to fade out the notes gracefully (if they can do). If this is false, the notes will all be cut off immediately.This method will be called automatically according to the midi data passed into renderNextBlock(), but may be called explicitly too.