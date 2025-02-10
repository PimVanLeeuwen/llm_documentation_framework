#### addDocument()


 bool MultiDocumentPanel::addDocument ( Component \* component, 
 
 Colour backgroundColour, 
 bool deleteWhenRemoved ) 

Adds a document component to the panel.If the number of documents would exceed the limit set by setMaximumNumDocuments() then this will fail and return false. (If it does fail, the component passedin will not be deleted, even if deleteWhenRemoved was set to true).The MultiDocumentPanel will deal with creating a window border to go around your component, so just pass in the bare content component here, no need to give it a ResizableWindow or DocumentWindow.Parameters

 component the component to add 
 
 backgroundColour the background colour to use to fill the component's window or tab 
 deleteWhenRemoved if true, then when the component is removed by closeDocumentAsync() or closeAllDocumentsAsync(), then it will be deleted. If false, then the caller must handle the component's deletion