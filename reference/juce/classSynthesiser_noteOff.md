#### noteOff()


 virtual void Synthesiser::noteOff ( int midiChannel, int midiNoteNumber, float velocity, bool allowTailOff ) virtual 
 

Triggers a noteoff event.This will turn off any voices that are playing a sound for the given note/channel.If allowTailOff is true, the voices will be allowed to fade out the notes gracefully (if they can do). If this is false, the notes will all be cut off immediately.This method will be called automatically according to the midi data passed into renderNextBlock(), but may be called explicitly too.The midiChannel parameter is the channel, between 1 and 16 inclusive.