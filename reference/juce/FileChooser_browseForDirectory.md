#### browseForDirectory()


 bool FileChooser::browseForDirectory ( ) 
 

Shows a dialog box to choose a directory.This will display the dialog box modally, using an "open directory" mode, so it will only allow directories to be returned, not files.Returnstrue if the user chose a directory and pressed 'ok', in which case, use the getResult() method to find out what they chose. Returns false if they cancelled instead. 
See alsobrowseForFileToOpen, browseForFileToSave