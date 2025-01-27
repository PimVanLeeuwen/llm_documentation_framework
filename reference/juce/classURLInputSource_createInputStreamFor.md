#### createInputStreamFor()


 InputStream \* URLInputSource::createInputStreamFor ( const String & relatedItemPath ) overridevirtual 
 

Returns a new InputStream to read an item, relative.Parameters

 relatedItemPath the relative pathname of the resource that is required 
 



Returnsan inputstream that the caller will delete, or nullptr if the item isn't found. Implements InputSource.