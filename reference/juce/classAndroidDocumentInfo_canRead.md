#### canRead()


 bool AndroidDocumentInfo::canRead ( ) const 
 

True if this process has permission to read this file.If this returns true, and the AndroidDocument refers to a file rather than a directory, then AndroidDocument::createInputStream should work on this document.References String::isNotEmpty().