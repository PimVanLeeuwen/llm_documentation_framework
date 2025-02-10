#### saveDocumentAsync()


 virtual void FileBasedDocument::saveDocumentAsync ( const File & file, std::function< void(Result)> callback ) protectedvirtual 
 

This method should try to write your document to the given file, then call the provided callback on the message thread, passing the result of the write.By default, this will synchronously call through to saveDocument.For longerrunning save operations, you may wish to override this function to run the save on a background thread, and then to call the callback later on the message thread to signal that the save has completed.