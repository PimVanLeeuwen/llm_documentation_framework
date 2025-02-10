#### setNextReadPosition()


 virtual void PositionableAudioSource::setNextReadPosition ( int64 newPosition ) pure virtual 
 

Tells the stream to move to a new position.Calling this indicates that the next call to AudioSource::getNextAudioBlock() should return samples from this position.Note that this may be called on a different thread to getNextAudioBlock(), so the subclass should make sure it's synchronised.Implemented in AudioFormatReaderSource, AudioTransportSource, BufferingAudioSource, and MemoryAudioSource.