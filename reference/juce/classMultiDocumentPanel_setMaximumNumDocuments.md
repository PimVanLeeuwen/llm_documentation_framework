#### setMaximumNumDocuments()


 void MultiDocumentPanel::setMaximumNumDocuments ( int maximumNumDocuments ) 
 

Sets a limit on how many windows can be open at once.If this is zero or less there's no limit (the default). addDocument() will fail if this number is exceeded.