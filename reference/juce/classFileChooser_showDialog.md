#### showDialog()


 bool FileChooser::showDialog ( int flags, 
 
 FilePreviewComponent \* previewComponent ) 

Runs a dialog box for the given set of option flags.The flag values used are those in FileBrowserComponent::FileChooserFlags.Returnstrue if the user chose a directory and pressed 'ok', in which case, use the getResult() method to find out what they chose. Returns false if they cancelled instead. 
See alsoFileBrowserComponent::FileChooserFlags