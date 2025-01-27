#### startVoice()


 void Synthesiser::startVoice ( SynthesiserVoice \* voice, SynthesiserSound \* sound, int midiChannel, int midiNoteNumber, float velocity ) protected 
 

Starts a specified voice playing a particular sound.You'll probably never need to call this, it's used internally by noteOn(), but may be needed by subclasses for custom behaviours.