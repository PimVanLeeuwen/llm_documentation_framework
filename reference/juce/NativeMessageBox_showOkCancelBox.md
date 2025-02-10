#### showOkCancelBox()


 static bool JUCE\_CALLTYPE NativeMessageBox::showOkCancelBox ( MessageBoxIconType iconType, const String & title, const String & message, Component \* associatedComponent = nullptr, ModalComponentManager::Callback \* callback = nullptr ) static 
 

Shows a dialog box with two buttons.Ideal for ok/cancel or yes/no choices. The return key can also be used to trigger the first button, and the escape key for the second button.If the callback parameter is null and modal loops are enabled, the box is shown modally, and the method will block until the user has clicked the button (or pressed the escape or return keys). If the callback parameter is nonnull, the box will be displayed and placed into a modal state, but this method will return immediately, and the callback will be invoked later when the user dismisses the box.Parameters

 iconType the type of icon to show. 
 
 title the headline to show at the top of the box. 
 message a longer, more descriptive message to show underneath the title. 
 associatedComponent if this is nonnull, it specifies the component that the alert window should be associated with. Depending on the look and feel, this might be used for positioning of the alert window. 
 callback if this is nonnull, the box will be launched asynchronously, returning immediately, and the callback will receive a call to its modalStateFinished() when the box is dismissed, with its parameter being 1 if the ok button was pressed, or 0 for cancel, The callback object will be owned and deleted by the system, so make sure that it works safely and doesn't keep any references to objects that might be deleted before it gets called. You can use the ModalCallbackFunction to easily pass in a lambda for this parameter. 



Returnstrue if button 1 was clicked, false if it was button 2. If the callback parameter is not null, the method always returns false, and the user's choice is delivered later by the callback.
See alsoModalCallbackFunction