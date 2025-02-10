#### drawChannels()


 void AudioThumbnail::drawChannels ( Graphics & g, const Rectangle< int > & area, double startTimeSeconds, double endTimeSeconds, float verticalZoomFactor ) overridevirtual 
 

Draws the waveforms for all channels in the thumbnail.This will call drawChannel() to render each of the thumbnail's channels, stacked above each other within the specified area.See alsodrawChannel Implements AudioThumbnailBase.