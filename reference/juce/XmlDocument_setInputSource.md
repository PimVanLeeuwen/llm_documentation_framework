#### setInputSource()


 void XmlDocument::setInputSource ( InputSource \* newSource ) noexcept 
 

Sets an input source object to use for parsing documents that reference external entities.If the document has been created from a file, this probably won't be needed, but if you're parsing some text and there might be a DTD that references external files, you may need to create a custom input source that can retrieve the other files it needs.The object that is passedin will be deleted automatically when no longer needed.See alsoInputSource