#### makeOptionsOk()


 static MessageBoxOptions MessageBoxOptions::makeOptionsOk ( MessageBoxIconType iconType, const String & title, const String & message, const String & buttonText = String(), Component \* associatedComponent = nullptr ) static 
 

Creates options suitable for a message box with a single button.If no button text is supplied, "OK" will be used.Referenced by StandalonePluginHolder::askUserToLoadState(), and StandalonePluginHolder::askUserToSaveState().