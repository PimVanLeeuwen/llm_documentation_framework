#### loadFromUserSpecifiedFile()


 Result FileBasedDocument::loadFromUserSpecifiedFile ( bool showMessageOnFailure ) 
 

Asks the user for a file and tries to load it.This will pop up a dialog box using the title, file extension and wildcard specified in the document's constructor, and asks the user for a file. If they pick one, the loadFrom() method is used to try to load it, optionally showing a message if it fails.Returnsa result indicating success; This will be a failure message if the user cancelled or if they picked a file which failed to load correctly 
See alsoloadFrom