#### setZoneLayout()


 void MPEInstrument::setZoneLayout ( MPEZoneLayout newLayout ) 
 

Resets the zone layout of the instrument to the one passed in.As a side effect, this will discard all currently playing notes, and call noteReleased for all of them.This will also disable legacy mode in case it was enabled previously.