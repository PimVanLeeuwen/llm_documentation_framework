#### noteOn()


 virtual void Synthesiser::noteOn ( int midiChannel, int midiNoteNumber, float velocity ) virtual 
 

Triggers a noteon event.The default method here will find all the sounds that want to be triggered by this note/channel. For each sound, it'll try to find a free voice, and use the voice to start playing the sound.Subclasses might want to override this if they need a more complex algorithm.This method will be called automatically according to the midi data passed into renderNextBlock(), but may be called explicitly too.The midiChannel parameter is the channel, between 1 and 16 inclusive.