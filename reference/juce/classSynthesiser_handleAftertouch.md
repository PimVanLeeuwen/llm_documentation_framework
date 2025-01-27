#### handleAftertouch()


 virtual void Synthesiser::handleAftertouch ( int midiChannel, int midiNoteNumber, int aftertouchValue ) virtual 
 

Sends an aftertouch message.This will send an aftertouch message to any voices that are playing sounds on the given midi channel and note number.This method will be called automatically according to the midi data passed into renderNextBlock(), but may be called explicitly too.Parameters

 midiChannel the midi channel, from 1 to 16 inclusive 
 
 midiNoteNumber the midi note number, 0 to 127 
 aftertouchValue the aftertouch value, between 0 and 127, as returned by MidiMessage::getAftertouchValue()