#### setReadTimeout()


 void BufferingAudioReader::setReadTimeout ( int timeoutMilliseconds ) noexcept 
 

Sets a number of milliseconds that the reader can block for in its readSamples() method before giving up and returning silence.A value of less that 0 means "wait forever". The default timeout is 0.