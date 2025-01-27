#### closeDocument()


 bool MultiDocumentPanel::closeDocument ( Component \* component, 
 
 bool checkItsOkToCloseFirst ) 

Closes one of the documents.If checkItsOkToCloseFirst is true, then the tryToCloseDocument() method will be called, and if it fails, this method will return false without closing the document.If checkItsOkToCloseFirst is false, then the documents will be closed unconditionally.The component will be deleted if the deleteWhenRemoved parameter was set to true when it was added with addDocument.See alsoaddDocument, closeAllDocuments