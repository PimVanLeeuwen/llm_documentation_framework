#### drawChannel()


 void AudioThumbnail::drawChannel ( Graphics & g, const Rectangle< int > & area, double startTimeSeconds, double endTimeSeconds, int channelNum, float verticalZoomFactor ) overridevirtual 
 

Draws the waveform for a channel.The waveform will be drawn within the specified rectangle, where startTime and endTime specify the times within the audio file that should be positioned at the left and right edges of the rectangle.The waveform will be scaled vertically so that a fullvolume sample will fill the rectangle vertically, but you can also specify an extra vertical scale factor with the verticalZoomFactor parameter.Implements AudioThumbnailBase.