#### setSource()


 void AudioSourcePlayer::setSource ( AudioSource \* newSource ) 
 

Changes the current audio source to play from.If the source passed in is already being used, this method will do nothing. If the source is not null, its prepareToPlay() method will be called before it starts being used for playback.If there's another source currently playing, its releaseResources() method will be called after it has been swapped for the new one.Parameters

 newSource the new source to use this will NOT be deleted by this object when no longer needed, so it's the caller's responsibility to manage it.