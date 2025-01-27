#### tryToCloseDocumentAsync()


 virtual void MultiDocumentPanel::tryToCloseDocumentAsync ( Component \* component, std::function< void(bool)> callback ) pure virtual 
 

A subclass must override this to say whether its currently ok for a document to be closed.This method is called by closeDocumentAsync() and closeAllDocumentsAsync() to indicate that a document should be saved if possible, ready for it to be closed.If the callback is called with a true argument, then it means the document is ok and can be closed.If the callback is called with a false argument, then it means that the closeDocumentAsync() method should stop and not close.Normally, you'd use this method to ask the user if they want to save any changes, then return true if the save operation went ok. If the user cancelled the save operation you could give a value of false to the callback to abort the close operation.If your component is based on the FileBasedDocument class, then you'd probably want to call FileBasedDocument::saveIfNeededAndUserAgreesAsync() and call the callback with true if this returned FileBasedDocument::savedOk.See alsocloseDocumentAsync, FileBasedDocument::saveIfNeededAndUserAgreesAsync()