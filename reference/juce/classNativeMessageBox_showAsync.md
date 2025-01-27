#### showAsync() [2/2]


 static void JUCE\_CALLTYPE NativeMessageBox::showAsync ( const MessageBoxOptions & options, std::function< void(int)> callback ) static 
 

Shows a dialog box using the specified options.The box will be displayed and placed into a modal state, but this method will return immediately, and the callback will be invoked later when the user dismisses the box.Parameters

 options the options to use when creating the dialog. 
 
 callback if this is nonnull, the callback will be called when the box is dismissed with the index of the button that was clicked as its argument. 



See alsoMessageBoxOptions