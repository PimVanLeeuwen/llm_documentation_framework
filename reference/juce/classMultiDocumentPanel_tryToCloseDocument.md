#### tryToCloseDocument()


 virtual bool MultiDocumentPanel::tryToCloseDocument ( Component \* component ) virtual 
 

A subclass must override this to say whether its currently ok for a document to be closed.This method is called by closeDocument() and closeAllDocuments() to indicate that a document should be saved if possible, ready for it to be closed.If this method returns true, then it means the document is ok and can be closed.If it returns false, then it means that the closeDocument() method should stop and not close.Normally, you'd use this method to ask the user if they want to save any changes, then return true if the save operation went ok. If the user cancelled the save operation you could return false here to abort the close operation.If your component is based on the FileBasedDocument class, then you'd probably want to call FileBasedDocument::saveIfNeededAndUserAgrees() and return true if this returned FileBasedDocument::savedOkSee alsocloseDocument, FileBasedDocument::saveIfNeededAndUserAgrees()