#### setChangedFlag()


 void FileBasedDocument::setChangedFlag ( bool hasChanged ) 
 

Sets the state of the 'changed' flag.The 'changed' flag is set to true when the changed() method is called use this method to reset it or to set it without also broadcasting a change message.See alsochanged, hasChangedSinceSaved