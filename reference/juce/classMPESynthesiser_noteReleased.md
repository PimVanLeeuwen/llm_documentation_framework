#### noteReleased()


 void MPESynthesiser::noteReleased ( MPENote finishedNote ) overrideprotectedvirtual 
 

Stops playing a note.This will be called whenever an MPE note is released (either by a noteoff message, or by a sustain/sostenuto pedal release for a note that already received a noteoff), and should therefore stop playing.This will find any voice that is currently playing finishedNote, turn its currently playing note off, and call its noteStopped callback.This method will be called automatically according to the midi data passed into renderNextBlock(). Do not call it yourself, otherwise the internal MPE note state will become inconsistent.Reimplemented from MPEInstrument::Listener.