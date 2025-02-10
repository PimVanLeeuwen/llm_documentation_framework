#### browseForFileToSave()


 bool FileChooser::browseForFileToSave ( bool warnAboutOverwritingExistingFiles ) 
 

Shows a dialog box to choose a file to save.This will display the dialog box modally, using an "save file" mode, so it will allow nonexistent files to be chosen, but not directories.Parameters

 warnAboutOverwritingExistingFiles if true, the dialog box will ask the user if they're sure they want to overwrite a file that already exists 
 



Returnstrue if the user chose a file and pressed 'ok', in which case, use the getResult() method to find out what the file was. Returns false if they cancelled instead. 
See alsobrowseForFileToOpen, browseForDirectory