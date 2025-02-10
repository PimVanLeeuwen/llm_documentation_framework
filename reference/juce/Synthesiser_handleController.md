#### handleController()


 virtual void Synthesiser::handleController ( int midiChannel, int controllerNumber, int controllerValue ) virtual 
 

Sends a midi controller message to any active voices.This will send a midi controller message to any voices that are playing sounds on the given midi channel.This method will be called automatically according to the midi data passed into renderNextBlock(), but may be called explicitly too.Parameters

 midiChannel the midi channel, from 1 to 16 inclusive 
 
 controllerNumber the midi controller type, as returned by MidiMessage::getControllerNumber() 
 controllerValue the midi controller value, between 0 and 127, as returned by MidiMessage::getControllerValue()