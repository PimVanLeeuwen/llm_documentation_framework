#### noteKeyStateChanged()


 virtual void MPEInstrument::Listener::noteKeyStateChanged ( MPENote changedNote ) virtual 
 

Implement this callback to be informed whether a currently playing MPE note's key state (whether the key is down and/or the note is sustained) has changed.Note: If the key state changes to MPENote::off, noteReleased is called instead.Reimplemented in MPESynthesiser.