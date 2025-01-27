#### prepareToPlay()


 virtual void AudioSource::prepareToPlay ( int samplesPerBlockExpected, double sampleRate ) pure virtual 
 

Tells the source to prepare for playing.An AudioSource has two states: prepared and unprepared.The prepareToPlay() method is guaranteed to be called at least once on an 'unprepared' source to put it into a 'prepared' state before any calls will be made to getNextAudioBlock(). This callback allows the source to initialise any resources it might need when playing.Once playback has finished, the releaseResources() method is called to put the stream back into an 'unprepared' state.Note that this method could be called more than once in succession without a matching call to releaseResources(), so make sure your code is robust and can handle that kind of situation.Parameters

 samplesPerBlockExpected the number of samples that the source will be expected to supply each time its getNextAudioBlock() method is called. This number may vary slightly, because it will be dependent on audio hardware callbacks, and these aren't guaranteed to always use a constant block size, so the source should be able to cope with small variations. 
 
 sampleRate the sample rate that the output will be used at this is needed by sources such as tone generators. 



See alsoreleaseResources, getNextAudioBlock Implemented in AudioAppComponent, AudioFormatReaderSource, AudioTransportSource, BufferingAudioSource, ChannelRemappingAudioSource, IIRFilterAudioSource, MemoryAudioSource, MixerAudioSource, ResamplingAudioSource, ReverbAudioSource, and ToneGeneratorAudioSource.