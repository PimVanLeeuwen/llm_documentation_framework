#### setFlushInterval()


 void AudioFormatWriter::ThreadedWriter::setFlushInterval ( int numSamplesPerFlush ) noexcept 
 

Sets how many samples should be written before calling the AudioFormatWriter::flush method.Set this to 0 to disable flushing (this is the default).