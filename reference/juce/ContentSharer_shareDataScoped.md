#### shareDataScoped()


 static ScopedMessageBox ContentSharer::shareDataScoped ( const MemoryBlock & mb, Callback callback, Component \* parent = nullptr ) staticnodiscard 
 

A convenience function to share arbitrary data.The data will be written to a temporary file and then that file will be shared. If you have your data stored on disk already, call shareFiles() instead.Upon completion you will receive a callback with a sharing result. Note: Sadly on Android the returned success flag may be wrong as there is no standard way the sharing targets report if the sharing operation succeeded. Also, the optional error message is always empty on Android.Parameters

 mb the data to share 
 
 callback a callback that will be called on the main thread when the sharing session ends 
 parent the component that should be used to host the sharing view