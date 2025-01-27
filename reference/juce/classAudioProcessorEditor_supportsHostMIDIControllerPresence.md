#### supportsHostMIDIControllerPresence()


 virtual bool AudioProcessorEditor::supportsHostMIDIControllerPresence ( bool hostMIDIControllerIsAvailable ) virtual 
 

Override this method to indicate if your editor supports the presence or absence of a hostprovided MIDI controller.Currently only AUv3 plugins support this functionality, and even then the host may choose to ignore this information.The default behaviour is to report support for both cases.