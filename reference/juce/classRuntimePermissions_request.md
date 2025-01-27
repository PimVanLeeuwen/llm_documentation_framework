#### request()


 static void RuntimePermissions::request ( PermissionID permission, Callback callback ) static 
 

Call this method to request a runtime permission.Parameters

 permission The PermissionID of the permission you want to request. 
 
 callback The callback to be called after the request has been granted or denied; the argument passed will be true if the permission has been granted and false otherwise. 


If no runtime request is required or possible to obtain the permission, the callback will be called immediately. The argument passed in will be true if the permission is granted or no permission is required on this platform, and false otherwise.If a runtime request is required to obtain the permission, the callback will be called asynchronously after the OS has granted or denied the requested permission (typically by displaying a dialog box to the user and waiting until the user has responded).Referenced by StandalonePluginHolder::StandalonePluginHolder().