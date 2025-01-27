#### shareFilesScoped()


 static ScopedMessageBox ContentSharer::shareFilesScoped ( const Array< URL > & files, Callback callback, Component \* parent = nullptr ) staticnodiscard 
 

Shares the given files.Each URL should be either a full file path or it should point to a resource within the application bundle. For resources on iOS it should be something like "content/image.png" if you want to specify a file from application bundle located in "content" directory. On Android you should specify only a filename, without an extension.Upon completion you will receive a callback with a sharing result. Note: Sadly on Android the returned success flag may be wrong as there is no standard way the sharing targets report if the sharing operation succeeded. Also, the optional error message is always empty on Android.Parameters

 files the files to share 
 
 callback a callback that will be called on the main thread when the sharing session ends 
 parent the component that should be used to host the sharing view