#### handleController()


 virtual void MPESynthesiser::handleController ( int , int , int ) virtual 
 

Callback for MIDI controller messages.The default implementation provided here does nothing; override this method if you need custom MIDI controller handling on top of MPE.This method will be called automatically according to the midi data passed into renderNextBlock().