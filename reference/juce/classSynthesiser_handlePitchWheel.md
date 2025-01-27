#### handlePitchWheel()


 virtual void Synthesiser::handlePitchWheel ( int midiChannel, int wheelValue ) virtual 
 

Sends a pitchwheel message to any active voices.This will send a pitchwheel message to any voices that are playing sounds on the given midi channel.This method will be called automatically according to the midi data passed into renderNextBlock(), but may be called explicitly too.Parameters

 midiChannel the midi channel, from 1 to 16 inclusive 
 
 wheelValue the wheel position, from 0 to 0x3fff, as returned by MidiMessage::getPitchWheelValue()