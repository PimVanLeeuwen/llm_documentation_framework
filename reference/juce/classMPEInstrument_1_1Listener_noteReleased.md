#### noteReleased()


 virtual void MPEInstrument::Listener::noteReleased ( MPENote finishedNote ) virtual 
 

Implement this callback to be informed whenever an MPE note is released (either by a noteoff message, or by a sustain/sostenuto pedal release for a note that already received a noteoff), and should therefore stop playing.Reimplemented in MPESynthesiser.