#### waitForNextAudioBlockReady()


 bool BufferingAudioSource::waitForNextAudioBlockReady ( const AudioSourceChannelInfo & info, 
 
 uint32 timeout ) 

A useful function to block until the next the buffer info can be filled.This is useful for offline rendering.