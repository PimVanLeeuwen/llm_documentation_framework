#### processNextMidiBuffer()


 void MPEZoneLayout::processNextMidiBuffer ( const MidiBuffer & buffer ) 
 

Pass incoming MIDI buffers to an object of this class if you want the zone layout to properly react to MPE RPN messages like an MPE device.MPEMessages::rpnNumber will add or remove zones; RPN 0 will set the pernote or master pitchbend ranges.Any other MIDI messages will be ignored by this class.See alsoMPEMessages