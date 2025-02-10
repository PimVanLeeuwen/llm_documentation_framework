#### getZoneLayout()


 MPEZoneLayout MPEInstrument::getZoneLayout ( ) const noexcept 
 

Returns the current zone layout of the instrument.This happens by value, to enforce threadsafety and class invariants.Note: If the instrument is in legacy mode, the return value of this method is unspecified.