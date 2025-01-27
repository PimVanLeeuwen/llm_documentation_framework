#### renderNextBlock()


template<typename floatType > 

 void MPESynthesiserBase::renderNextBlock ( AudioBuffer< floatType > & outputAudio, 
 
 const MidiBuffer & inputMidi, 
 int startSample, 
 int numSamples ) 

Creates the next block of audio output.Call this to make sound. This will chop up the AudioBuffer into subBlock pieces separated by events in the MIDI buffer, and then call renderNextSubBlock on each one of them. In between you will get calls to noteAdded/Changed/Finished, where you can update parameters that depend on those notes to use for your audio rendering.Parameters

 outputAudio Buffer into which audio will be rendered 
 
 inputMidi MIDI events to process 
 startSample The first sample to process in both buffers 
 numSamples The number of samples to process