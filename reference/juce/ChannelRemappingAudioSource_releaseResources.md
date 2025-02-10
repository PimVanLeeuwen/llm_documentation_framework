#### releaseResources()


 void ChannelRemappingAudioSource::releaseResources ( ) overridevirtual 
 

Allows the source to release anything it no longer needs after playback has stopped.This will be called when the source is no longer going to have its getNextAudioBlock() method called, so it should release any spare memory, etc. that it might have allocated during the prepareToPlay() call.Note that there's no guarantee that prepareToPlay() will actually have been called before releaseResources(), and it may be called more than once in succession, so make sure your code is robust and doesn't make any assumptions about when it will be called.See alsoprepareToPlay, getNextAudioBlock Implements AudioSource.