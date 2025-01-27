#### browseForFileToOpen()


 bool FileChooser::browseForFileToOpen ( FilePreviewComponent \* previewComponent = nullptr ) 
 

Shows a dialog box to choose a file to open.This will display the dialog box modally, using an "open file" mode, so that it won't allow nonexistent files or directories to be chosen.Parameters

 previewComponent an optional component to display inside the dialog box to show special info about the files that the user is browsing. The component will not be deleted by this object, so the caller must take care of it. 
 



Returnstrue if the user selected a file, in which case, use the getResult() method to find out what it was. Returns false if they cancelled instead. 
See alsobrowseForFileToSave, browseForDirectory