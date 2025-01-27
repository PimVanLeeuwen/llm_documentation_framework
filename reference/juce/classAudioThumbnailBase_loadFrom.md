#### loadFrom()


 virtual bool AudioThumbnailBase::loadFrom ( InputStream & input ) pure virtual 
 

Reloads the low res thumbnail data from an input stream.This is not an audio file stream! It takes a stream of thumbnail data that would previously have been created by the saveTo() method.See alsosaveTo Implemented in AudioThumbnail.