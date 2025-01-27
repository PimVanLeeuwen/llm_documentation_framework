#### setZoneLayout()


 static MidiBuffer MPEMessages::setZoneLayout ( MPEZoneLayout layout ) static 
 

Returns the sequence of MIDI messages that, if sent to an Expressive MIDI device, will reset the whole MPE zone layout of the device to the layout passed in.This will first clear the current lower and upper zones, then then set the zones contained in the passedin zone layout, and set their pernote and master pitchbend ranges to their current values.

Member Data Documentation