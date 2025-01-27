#### createInputStreamFor()


 virtual InputStream \* InputSource::createInputStreamFor ( const String & relatedItemPath ) pure virtual 
 

Returns a new InputStream to read an item, relative.Parameters

 relatedItemPath the relative pathname of the resource that is required 
 



Returnsan inputstream that the caller will delete, or nullptr if the item isn't found. Implemented in AndroidDocumentInputSource, FileInputSource, and URLInputSource.