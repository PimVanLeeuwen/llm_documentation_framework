#### read() [3/3]


 bool AudioFormatReader::read ( AudioBuffer< float > \* buffer, 
 
 int startSampleInDestBuffer, 
 int numSamples, 
 int64 readerStartSample, 
 bool useReaderLeftChan, 
 bool useReaderRightChan ) 

Fills a section of an AudioBuffer from this reader.This will convert the reader's fixed or floatingpoint data to the buffer's floatingpoint format, and will try to intelligently cope with mismatches between the number of channels in the reader and the buffer.Returnstrue if the operation succeeded, false if there was an error. Note that reading sections of data beyond the extent of the stream isn't an error the reader should just return zeros for these regions