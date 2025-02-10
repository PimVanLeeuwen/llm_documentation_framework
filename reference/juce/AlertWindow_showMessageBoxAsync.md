#### showMessageBoxAsync()


 static void JUCE\_CALLTYPE AlertWindow::showMessageBoxAsync ( MessageBoxIconType iconType, const String & title, const String & message, const String & buttonText = String(), Component \* associatedComponent = nullptr, ModalComponentManager::Callback \* callback = nullptr ) static 
 

Shows a dialog box that just has a message and a single button to get rid of it.The box will be displayed and placed into a modal state, but this method will return immediately, and if a callback was supplied, it will be invoked later when the user dismisses the box.Parameters

 iconType the type of icon to show 
 
 title the headline to show at the top of the box 
 message a longer, more descriptive message to show underneath the headline 
 buttonText the text to show in the button if this string is empty, the default string "OK" (or a localised version) will be used. 
 associatedComponent if this is nonnull, it specifies the component that the alert window should be associated with. Depending on the look and feel, this might be used for positioning of the alert window. 
 callback if this is nonnull, the callback will receive a call to its modalStateFinished() when the box is dismissed. The callback object will be owned and deleted by the system, so make sure that it works safely and doesn't keep any references to objects that might be deleted before it gets called.