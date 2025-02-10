#### write()


 bool AudioFormatWriter::ThreadedWriter::write ( const float \*const \* data, 
 
 int numSamples ) 

Pushes some incoming audio data into the FIFO.If there's enough free space in the buffer, this will add the data to it,If the FIFO is too full to accept this many samples, the method will return false then you could either wait until the background thread has had time to consume some of the buffered data and try again, or you can give up and lost this block.The data must be an array containing the same number of channels as the AudioFormatWriter object is using. None of these channels can be null.