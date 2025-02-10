#### handleProgramChange()


 virtual void Synthesiser::handleProgramChange ( int midiChannel, int programNumber ) virtual 
 

Can be overridden to handle an incoming program change message.The base class implementation of this has no effect, but you may want to make your own synth react to program changes.