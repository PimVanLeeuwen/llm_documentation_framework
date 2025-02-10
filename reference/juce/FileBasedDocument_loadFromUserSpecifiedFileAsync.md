#### loadFromUserSpecifiedFileAsync()


 void FileBasedDocument::loadFromUserSpecifiedFileAsync ( bool showMessageOnFailure, 
 
 std::function< void(Result)> callback ) 

Asks the user for a file and tries to load it.This will pop up a dialog box using the title, file extension and wildcard specified in the document's constructor, and asks the user for a file. If they pick one, the loadFrom() method is used to try to load it, optionally showing a message if it fails. The result of the operation is provided in the callback function.See alsoloadFrom