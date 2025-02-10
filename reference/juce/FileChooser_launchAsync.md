#### launchAsync()


 void FileChooser::launchAsync ( int flags, 
 
 std::function< void(const FileChooser &)> , 
 FilePreviewComponent \* previewComponent = nullptr ) 

Use this method to launch the file browser window asynchronously.This will create a file browser dialog based on the settings in this structure and will launch it modally, returning immediately.You must specify a callback which is called when the file browser is cancelled or a file is selected. To abort the file selection, simply delete the FileChooser object.You must ensure that the lifetime of the callback object is longer than the lifetime of the filechooser.Referenced by StandalonePluginHolder::askUserToLoadState(), and StandalonePluginHolder::askUserToSaveState().