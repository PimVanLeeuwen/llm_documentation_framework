#### setMidiOutput()


 void AudioProcessorPlayer::setMidiOutput ( MidiOutput \* midiOutputToUse ) 
 

Sets the MIDI output that should be used, if required.The MIDI output will not be deleted or owned by this object. If the MIDI output is deleted, pass a nullptr to this method.