#### isKeySignatureMajorKey()


 bool MidiMessage::isKeySignatureMajorKey ( ) const noexcept 
 

Returns true if this keysignature event is major, or false if it's minor.This method must only be called if isKeySignatureMetaEvent() is true.