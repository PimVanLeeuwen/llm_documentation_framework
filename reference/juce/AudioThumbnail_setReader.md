#### setReader()


 void AudioThumbnail::setReader ( AudioFormatReader \* newReader, int64 hashCode ) overridevirtual 
 

Gives the thumbnail an AudioFormatReader to use directly.This will start parsing the audio in a background thread (unless the hash code can be lookedup successfully in the thumbnail cache). Note that the reader object will be held by the thumbnail and deleted later when no longer needed. The thumbnail will actually keep hold of this reader until you clear the thumbnail or change the input source, so the file will be held open for all this time. If you don't want the thumbnail to keep a file handle open continuously, you should use the setSource() method instead, which will only open the file when it needs to.Implements AudioThumbnailBase.