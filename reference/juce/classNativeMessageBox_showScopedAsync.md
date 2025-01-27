#### showScopedAsync()


 static ScopedMessageBox NativeMessageBox::showScopedAsync ( const MessageBoxOptions & options, std::function< void(int)> callback ) staticnodiscard 
 

Shows a dialog box using the specified options.The box will be displayed and placed into a modal state, but this method will return immediately, and the callback will be invoked later when the user dismisses the box.This function is always asynchronous, even if the callback is null.For consistency with AlertWindow, the result codes returned by the alert window are as follows.One button:button[0] returns 0Two buttons:button[0] returns 1button[1] returns 0Three buttons:button[0] returns 1button[1] returns 2button[2] returns 0Another way of expressing this is that, when there are N buttons, then the result code for button X is equal to ((X + 1) % N).Parameters

 options the options to use when creating the dialog. 
 
 callback if this is nonnull, the callback will receive a call to its modalStateFinished() when the box is dismissed with the index of the button that was clicked as its argument. The callback object will be owned and deleted by the system, so make sure that it works safely and doesn't keep any references to objects that might be deleted before it gets called. 



Returnsa ScopedMessageBox instance. The message box will remain visible for no longer than the ScopedMessageBox remains alive.
See alsoMessageBoxOptions