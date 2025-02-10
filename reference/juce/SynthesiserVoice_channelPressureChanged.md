#### channelPressureChanged()


 virtual void SynthesiserVoice::channelPressureChanged ( int newChannelPressureValue ) virtual 
 

Called to let the voice know that the channel pressure has changed.This will be called during the rendering callback, so must be fast and threadsafe.