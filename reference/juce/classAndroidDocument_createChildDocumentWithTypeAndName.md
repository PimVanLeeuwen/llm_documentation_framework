#### createChildDocumentWithTypeAndName()


 AndroidDocument AndroidDocument::createChildDocumentWithTypeAndName ( const String & type, 
 
 const String & name ) const 

Attempts to create a new nested document with a particular type and name.The type should be a standard MIME type string, e.g. "image/png", "text/plain".The file name doesn't need to contain an extension, as this information is passed via the type argument. If this document is Filebased rather than URLbased, then an appropriate file extension will be chosen based on the MIME type.On failure, the returned AndroidDocument may be invalid, and will return false from hasValue().