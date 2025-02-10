#### notePitchbendChanged()


 virtual void MPEInstrument::Listener::notePitchbendChanged ( MPENote changedNote ) virtual 
 

Implement this callback to be informed whenever a currently playing MPE note's pitchbend value changes.Note: This can happen if the note itself is bent, if there is a master channel pitchbend event, or if both occur simultaneously. Call MPENote::getFrequencyInHertz to get the effective note frequency.Reimplemented in MPESynthesiser.