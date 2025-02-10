#### loadFromAsync()


 void FileBasedDocument::loadFromAsync ( const File & fileToLoadFrom, 
 
 bool showMessageOnFailure, 
 std::function< void(Result)> callback ) 

Tries to open a file.The callback is called with the result indicating whether the new file loaded successfully, or the error message if it failed.If the file opens correctly the document's file (see the getFile() method) is set to this new one; if it fails, the document's file is left unchanged, and optionally a message box is shown telling the user there was an error.See alsoloadDocumentAsync, loadFromUserSpecifiedFileAsync