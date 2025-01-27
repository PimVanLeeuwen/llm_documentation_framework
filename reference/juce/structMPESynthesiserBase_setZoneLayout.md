#### setZoneLayout()


 void MPESynthesiserBase::setZoneLayout ( MPEZoneLayout newLayout ) 
 

Resets the synthesiser's internal MPE zone layout to the one passed in.As a side effect, this will discard all currently playing notes, call noteReleased for all of them, and disable legacy mode (if previously enabled).