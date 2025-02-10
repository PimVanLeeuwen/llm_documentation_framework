#### setCurrentPlaybackSampleRate()


 virtual void SynthesiserVoice::setCurrentPlaybackSampleRate ( double newRate ) virtual 
 

Changes the voice's reference sample rate.The rate is set so that subclasses know the output rate and can set their pitch accordingly.This method is called by the synth, and subclasses can access the current rate with the currentSampleRate member.