#### setPosition()


 void AudioTransportSource::setPosition ( double newPosition ) 
 

Changes the current playback position in the source stream.The next time the getNextAudioBlock() method is called, this is the time from which it'll read data.Parameters

 newPosition the new playback position in seconds 
 



See alsogetCurrentPosition