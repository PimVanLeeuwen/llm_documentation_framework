#### saveAsync()


 void FileBasedDocument::saveAsync ( bool askUserForFileIfNotSpecified, 
 
 bool showMessageOnFailure, 
 std::function< void(SaveResult)> callback ) 

Tries to save the document to the last file it was saved or loaded from.This will always try to write to the file, even if the document isn't flagged as having changed.Parameters

 askUserForFileIfNotSpecified if there's no file currently specified and this is true, it will prompt the user to pick a file, as if saveAsInteractive() was called. 
 
 showMessageOnFailure if true it will show a warning message when if the save operation fails 
 callback called after the save operation with the result 



See alsosaveIfNeededAndUserAgrees, saveAs, saveAsInteractive