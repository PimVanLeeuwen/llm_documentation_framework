#### closeAllDocumentsAsync()


 void MultiDocumentPanel::closeAllDocumentsAsync ( bool checkItsOkToCloseFirst, 
 
 std::function< void(bool)> callback ) 

Tries to close all the documents.If checkItsOkToCloseFirst is true, then the tryToCloseDocumentAsync() method will be called for each open document, and any of these calls fails, this method will stop and provide an argument of false to the callback, leaving some documents still open.If checkItsOkToCloseFirst is false, then all documents will be closed unconditionally.See alsocloseDocumentAsync