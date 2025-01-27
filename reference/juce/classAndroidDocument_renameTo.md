#### renameTo()


 bool AndroidDocument::renameTo ( const String & newDisplayName ) 
 

Renames the document, and returns true on success.This may cause the document's URI and metadata to change, so ensure to invalidate any cached information about the document (URLs, AndroidDocumentInfo instances) after calling this function.