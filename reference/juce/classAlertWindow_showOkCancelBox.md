#### showOkCancelBox()


 static bool JUCE\_CALLTYPE AlertWindow::showOkCancelBox ( MessageBoxIconType iconType, const String & title, const String & message, const String & button1Text = String(), const String & button2Text = String(), Component \* associatedComponent = nullptr, ModalComponentManager::Callback \* callback = nullptr ) static 
 

Shows a dialog box with two buttons.Ideal for ok/cancel or yes/no choices. The return key can also be used to trigger the first button, and the escape key for the second button.If JUCE\_MODAL\_LOOPS\_PERMITTED is not defined or the callback parameter is nonnull, this function will return immediately. The object passed as the callback argument will receive the result of the alert window asynchronously. Otherwise, if JUCE\_MODAL\_LOOPS\_PERMITTED is defined and the callback parameter is null, the box is shown modally, and the method will block until the user has clicked the button (or pressed the escape or return keys). This mode of operation can cause problems, especially in plugins, so it is not recommended.Parameters

 iconType the type of icon to show 
 
 title the headline to show at the top of the box 
 message a longer, more descriptive message to show underneath the headline 
 button1Text the text to show in the first button if this string is empty, the default string "OK" (or a localised version of it) will be used. 
 button2Text the text to show in the second button if this string is empty, the default string "cancel" (or a localised version of it) will be used. 
 associatedComponent if this is nonnull, it specifies the component that the alert window should be associated with. Depending on the look and feel, this might be used for positioning of the alert window. 
 callback if this is nonnull, the menu will be launched asynchronously, returning immediately, and the callback will receive a call to its modalStateFinished() when the box is dismissed, with its parameter being 1 if the ok button was pressed, or 0 for cancel. The callback object will be owned and deleted by the system, so make sure that it works safely and doesn't keep any references to objects that might be deleted before it gets called. 



Returnstrue if button 1 was clicked, false if it was button 2. If the callback parameter is not null, the method always returns false, and the user's choice is delivered later by the callback.