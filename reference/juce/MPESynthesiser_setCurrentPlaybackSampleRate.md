#### setCurrentPlaybackSampleRate()


 void MPESynthesiser::setCurrentPlaybackSampleRate ( double newRate ) overridevirtual 
 

Tells the synthesiser what the sample rate is for the audio it's being used to render.This overrides the implementation in MPESynthesiserBase, to additionally propagate the new value to the voices so that they can use it to render the correct pitches.Reimplemented from MPESynthesiserBase.