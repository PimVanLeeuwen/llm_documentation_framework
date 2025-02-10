#### createInputStream()


 virtual InputStream \* InputSource::createInputStream ( ) pure virtual 
 

Returns a new InputStream to read this item.Returnsan inputstream that the caller will delete, or nullptr if the filename isn't found. Implemented in AndroidDocumentInputSource, FileInputSource, and URLInputSource.