#### hostMIDIControllerIsAvailable()


 virtual void AudioProcessorEditor::hostMIDIControllerIsAvailable ( bool controllerIsAvailable ) virtual 
 

Called to indicate if a host is providing a MIDI controller when the host reconfigures its layout.Use this as an opportunity to hide or display your own onscreen keyboard or other input component.Currently only AUv3 plugins support this functionality.