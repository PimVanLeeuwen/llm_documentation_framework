#### createReaderFor() [2/2]


 AudioFormatReader \* AudioFormatManager::createReaderFor ( std::unique\_ptr< InputStream > audioFileStream ) 
 

Searches through the known formats to try to create a suitable reader for this stream.The stream object that is passedin will be deleted by this method or by the reader that is returned, so the caller should not keep any references to it.The stream that is passedin must be capable of being repositioned so that all the formats can have a go at opening it.If none of the registered formats can open the stream, it'll return nullptr. If it returns a reader, it's the caller's responsibility to delete the reader.