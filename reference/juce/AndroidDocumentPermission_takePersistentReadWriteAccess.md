#### takePersistentReadWriteAccess()


 static void AndroidDocumentPermission::takePersistentReadWriteAccess ( const URL & ) static 
 

Gives your app access to a particular document or tree, even after the device is rebooted.If you want to persist access to a folder selected through a native file chooser, make sure to pass the exact URL returned by the file picker. Do NOT call AndroidDocument::fromTree and then pass the result of getUrl to this function, as the resulting URL may differ from the result of the file picker.