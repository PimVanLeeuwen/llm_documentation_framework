#### shareTextScoped()


 static ScopedMessageBox ContentSharer::shareTextScoped ( const String & text, Callback callback, Component \* parent = nullptr ) staticnodiscard 
 

Shares the given text.Upon completion you will receive a callback with a sharing result. Note: Sadly on Android the returned success flag may be wrong as there is no standard way the sharing targets report if the sharing operation succeeded. Also, the optional error message is always empty on Android.Parameters

 text the text to share 
 
 callback a callback that will be called on the main thread when the sharing session ends 
 parent the component that should be used to host the sharing view