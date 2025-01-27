#### loadDocumentAsync()


 virtual void FileBasedDocument::loadDocumentAsync ( const File & file, std::function< void(Result)> callback ) protectedvirtual 
 

This method should try to load your document from the given file, then call the provided callback on the message thread, passing the result of the load.By default, this will synchronously call through to loadDocument.For longerrunning load operations, you may wish to override this function to run the load on a background thread, and then to call the callback later on the message thread to signal that the load has completed.