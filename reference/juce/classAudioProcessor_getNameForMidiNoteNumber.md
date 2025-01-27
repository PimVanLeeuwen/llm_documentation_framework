#### getNameForMidiNoteNumber()


 virtual std::optional< String > AudioProcessor::getNameForMidiNoteNumber ( int note, int midiChannel ) virtual 
 

Returns a custom name for a MIDI note number.This method allows the host to query your plugin for a custom name to display for a given MIDI note number. It's useful for plugins that work with drum kits, microtonal scales, or other mappings.Parameters

 note The MIDI note number for which the name is being requested. Some DAWs can request a note range outside of the standard [0127]. Ensure your plugin can handle this. 
 
 midiChannel The MIDI channel associated with the note. This is a 1based index (116). Use this parameter if your plugin provides channelspecific note mappings.