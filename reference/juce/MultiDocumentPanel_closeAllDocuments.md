#### closeAllDocuments()


 bool MultiDocumentPanel::closeAllDocuments ( bool checkItsOkToCloseFirst ) 
 

Tries to close all the documents.If checkItsOkToCloseFirst is true, then the tryToCloseDocument() method will be called for each open document, and any of these calls fails, this method will stop and return false, leaving some documents still open.If checkItsOkToCloseFirst is false, then all documents will be closed unconditionally.See alsocloseDocument