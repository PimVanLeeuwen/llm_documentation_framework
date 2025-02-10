#### saveAsAsync()


 void FileBasedDocument::saveAsAsync ( const File & newFile, 
 
 bool warnAboutOverwritingExistingFiles, 
 bool askUserForFileIfNotSpecified, 
 bool showMessageOnFailure, 
 std::function< void(SaveResult)> callback ) 

Tries to save the document to a specified file.If this succeeds, it'll also change the document's internal file (as returned by the getFile() method). If it fails, the file will be left unchanged.Parameters

 newFile the file to try to write to 
 
 warnAboutOverwritingExistingFiles if true and the file exists, it'll ask the user first if they want to overwrite it 
 askUserForFileIfNotSpecified if the file is nonexistent and this is true, it'll use the saveAsInteractive() method to ask the user for a filename 
 showMessageOnFailure if true and the write operation fails, it'll show a message box to warn the user 
 callback called with the result of the save operation 



See alsosaveIfNeededAndUserAgreesAsync, saveAsync, saveAsInteractiveAsync