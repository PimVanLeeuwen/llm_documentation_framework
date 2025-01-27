#### buffer


 AudioBuffer<float>\* AudioSourceChannelInfo::buffer 
 

The destination buffer to fill with audio data.When the AudioSource::getNextAudioBlock() method is called, the active section of this buffer should be filled with whatever output the source produces.Only the samples specified by the startSample and numSamples members of this structure should be affected by the call.The contents of the buffer when it is passed to the AudioSource::getNextAudioBlock() method can be treated as the input if the source is performing some kind of filter operation, but should be cleared if this is not the case the clearActiveBufferRegion() is a handy way of doing this.The number of channels in the buffer could be anything, so the AudioSource must cope with this in whatever way is appropriate for its function.