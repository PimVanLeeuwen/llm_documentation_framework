#### browseForMultipleFilesOrDirectories()


 bool FileChooser::browseForMultipleFilesOrDirectories ( FilePreviewComponent \* previewComponent = nullptr ) 
 

Same as browseForFileToOpen, but allows the user to select multiple files and directories.The files that are returned can be obtained by calling getResults(). See browseForFileToOpen() for more info about the behaviour of this method.