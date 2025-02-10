#### handleProgramChange()


 virtual void MPESynthesiser::handleProgramChange ( int , int ) virtual 
 

Callback for MIDI program change messages.The default implementation provided here does nothing; override this method if you need to handle those messages.This method will be called automatically according to the midi data passed into renderNextBlock().