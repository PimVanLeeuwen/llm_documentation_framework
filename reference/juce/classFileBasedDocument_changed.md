#### changed()


 virtual void FileBasedDocument::changed ( ) virtual 
 

Called to indicate that the document has changed and needs saving.This method will also trigger a change message to be sent out using the ChangeBroadcaster base class.After calling the method, the hasChangedSinceSaved() method will return true, until it is reset either by saving to a file or using the setChangedFlag() method.See alsohasChangedSinceSaved, setChangedFlag