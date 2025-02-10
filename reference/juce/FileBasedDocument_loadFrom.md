#### loadFrom()


 Result FileBasedDocument::loadFrom ( const File & fileToLoadFrom, 
 
 bool showMessageOnFailure, 
 bool showWaitCursor = true ) 

Tries to open a file.If the file opens correctly the document's file (see the getFile() method) is set to this new one; if it fails, the document's file is left unchanged, and optionally a message box is shown telling the user there was an error.ReturnsA result indicating whether the new file loaded successfully, or the error message if it failed. 
See alsoloadDocument, loadFromUserSpecifiedFile