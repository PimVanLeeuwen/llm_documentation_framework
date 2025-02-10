#### setCurrentPlaybackSampleRate()


 virtual void Synthesiser::setCurrentPlaybackSampleRate ( double sampleRate ) virtual 
 

Tells the synthesiser what the sample rate is for the audio it's being used to render.This value is propagated to the voices so that they can use it to render the correct pitches.