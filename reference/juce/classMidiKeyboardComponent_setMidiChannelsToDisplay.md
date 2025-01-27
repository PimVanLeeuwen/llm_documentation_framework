#### setMidiChannelsToDisplay()


 void MidiKeyboardComponent::setMidiChannelsToDisplay ( int midiChannelMask ) 
 

Sets a mask to indicate which incoming midi channels should be represented by key movements.The mask is a set of bits, where bit 0 = midi channel 1, bit 1 = midi channel 2, etc.If the MidiKeyboardState has a key down for any of the channels whose bits are set in this mask, the onscreen keys will also go down.By default, this mask is set to 0xffff (all channels displayed).See alsosetMidiChannel