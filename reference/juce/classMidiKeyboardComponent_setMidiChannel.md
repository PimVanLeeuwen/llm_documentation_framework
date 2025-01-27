#### setMidiChannel()


 void MidiKeyboardComponent::setMidiChannel ( int midiChannelNumber ) 
 

Changes the midi channel number that will be used for events triggered by clicking on the component.The channel must be between 1 and 16 (inclusive). This is the channel that will be passed on to the MidiKeyboardState::noteOn() method when the user clicks the component.Although this is the channel used for outgoing events, the component can display incoming events from more than one channel see setMidiChannelsToDisplay()See alsosetVelocity