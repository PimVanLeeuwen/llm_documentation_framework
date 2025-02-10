#### setSavePoint()


 void CodeDocument::setSavePoint ( ) noexcept 
 

Makes a note that the document's current state matches the one that is saved.After this has been called, hasChangedSinceSavePoint() will return false until the document has been altered, and then it'll start returning true. If the document is altered, but then undone until it gets back to this state, hasChangedSinceSavePoint() will again return false.See alsohasChangedSinceSavePoint