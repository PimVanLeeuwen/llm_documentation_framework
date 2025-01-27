#### getSuggestedSaveAsFile()


 virtual File FileBasedDocument::getSuggestedSaveAsFile ( const File & defaultFile ) protectedvirtual 
 

This is called by saveAsInteractiveAsync() to allow you to optionally customise the filename that the user is presented with in the save dialog.The defaultFile parameter is an initial suggestion based on what the class knows about the current document you can return a variation on this file with a different extension, etc, or just return something completely different.