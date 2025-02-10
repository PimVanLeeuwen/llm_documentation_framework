#### setSource()


 virtual bool AudioThumbnailBase::setSource ( InputSource \* newSource ) pure virtual 
 

Specifies the file or stream that contains the audio file.For a file, just callsetSource (new FileInputSource (file))
AudioThumbnailBase::setSourcevirtual bool setSource(InputSource \*newSource)=0Specifies the file or stream that contains the audio file.
FileInputSourceA type of InputSource that represents a normal file.Definition juce\_FileInputSource.h:50
You can pass a nullptr in here to clear the thumbnail. The source that is passed in will be deleted by this object when it is no longer needed.Returnstrue if the source could be opened as a valid audio file, false if this failed for some reason. Implemented in AudioThumbnail.