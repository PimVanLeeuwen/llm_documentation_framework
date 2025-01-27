#### moveDocumentFromParentToParent()


 bool AndroidDocument::moveDocumentFromParentToParent ( const AndroidDocument & currentParent, 
 
 const AndroidDocument & newParent ) 

Experimental: Attempts to move this document from one parent to another, and returns true on success.This may cause the document's URI and metadata to change, so ensure to invalidate any cached information about the document (URLs, AndroidDocumentInfo instances) after calling this function.This function may fail if the document doesn't allow moving, and when using URIbased documents on devices with API level 23 or lower.