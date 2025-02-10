#### paintChannel()


 virtual void AudioVisualiserComponent::paintChannel ( Graphics & , Rectangle< float > bounds, const Range< float > \* levels, int numLevels, int nextSample ) virtual 
 

Draws a channel of audio data in the given bounds.The default implementation just calls getChannelAsPath() and fits this into the given area. You may want to override this to draw things differently.