#### getNextAudioBlock()


 void AudioAppComponent::getNextAudioBlock ( const AudioSourceChannelInfo & bufferToFill ) overridepure virtual 
 

Called repeatedly to fetch subsequent blocks of audio data.After calling the prepareToPlay() method, this callback will be made each time the audio playback hardware (or whatever other destination the audio data is going to) needs another block of data.It will generally be called on a highpriority system thread, or possibly even an interrupt, so be careful not to do too much work here, as that will cause audio glitches!See alsoAudioSourceChannelInfo, prepareToPlay, releaseResources Implements AudioSource.