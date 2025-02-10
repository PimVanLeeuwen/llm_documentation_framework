#### isGranted()


 static bool RuntimePermissions::isGranted ( PermissionID permission ) static 
 

Returns true if the app has been already granted this permission, either via a previous runtime request or otherwise, or no permission is necessary.Note that this can be false even if isRequired returns false. In this case, the permission can not be obtained at all at runtime.Referenced by StandalonePluginHolder::StandalonePluginHolder().