#### addInputSource()


 void MixerAudioSource::addInputSource ( AudioSource \* newInput, 
 
 bool deleteWhenRemoved ) 

Adds an input source to the mixer.If the mixer is running you'll need to make sure that the input source is ready to play by calling its prepareToPlay() method before adding it. If the mixer is stopped, then its input sources will be automatically prepared when the mixer's prepareToPlay() method is called.Parameters

 newInput the source to add to the mixer 
 
 deleteWhenRemoved if true, then this source will be deleted when no longer needed by the mixer.