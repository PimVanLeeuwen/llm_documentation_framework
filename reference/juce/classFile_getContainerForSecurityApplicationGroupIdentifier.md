#### getContainerForSecurityApplicationGroupIdentifier()


 static File File::getContainerForSecurityApplicationGroupIdentifier ( const String & appGroup ) static 
 

Returns the path to the container shared by all apps with the provided app group ID.You must pass one of the app group IDs listed in your app's entitlements file.On failure, this function may return a nonexistent file, so you should check that the path exists and is writable before trying to use it.