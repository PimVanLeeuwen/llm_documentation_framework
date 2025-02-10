#### handleChannelPressure()


 virtual void Synthesiser::handleChannelPressure ( int midiChannel, int channelPressureValue ) virtual 
 

Sends a channel pressure message.This will send a channel pressure message to any voices that are playing sounds on the given midi channel.This method will be called automatically according to the midi data passed into renderNextBlock(), but may be called explicitly too.Parameters

 midiChannel the midi channel, from 1 to 16 inclusive 
 
 channelPressureValue the pressure value, between 0 and 127, as returned by MidiMessage::getChannelPressureValue()