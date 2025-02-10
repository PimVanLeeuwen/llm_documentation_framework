#### getFile()


 const File & FileBasedDocument::getFile ( ) const 
 

Returns the file that this document was last successfully saved or loaded from.When the document object is created, this will be set to File().It is changed when one of the load or save methods is used, or when setFile() is used to explicitly set it.