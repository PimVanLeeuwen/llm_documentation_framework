#### closeDocumentAsync()


 void MultiDocumentPanel::closeDocumentAsync ( Component \* component, 
 
 bool checkItsOkToCloseFirst, 
 std::function< void(bool)> callback ) 

Closes one of the documents.If checkItsOkToCloseFirst is true, then the tryToCloseDocumentAsync() method will be called, and if it fails, this method will call the callback with a false argument without closing the document.If checkItsOkToCloseFirst is false, then the documents will be closed unconditionally.The component will be deleted if the deleteWhenRemoved parameter was set to true when it was added with addDocument.See alsoaddDocument, closeAllDocumentsAsync