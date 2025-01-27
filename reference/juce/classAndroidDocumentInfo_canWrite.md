#### canWrite()


 bool AndroidDocumentInfo::canWrite ( ) const 
 

True if this is a document that can be written, or a directory that can be modified.If this returns true, and the AndroidDocument refers to a file rather than a directory, then AndroidDocument::createOutputStream should work on this document.References String::isNotEmpty().