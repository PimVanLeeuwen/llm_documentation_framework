#### showYesNoCancelBox()


 static int JUCE\_CALLTYPE AlertWindow::showYesNoCancelBox ( MessageBoxIconType iconType, const String & title, const String & message, const String & button1Text = String(), const String & button2Text = String(), const String & button3Text = String(), Component \* associatedComponent = nullptr, ModalComponentManager::Callback \* callback = nullptr ) static 
 

Shows a dialog box with three buttons.Ideal for yes/no/cancel boxes.The escape key can be used to trigger the third button.If JUCE\_MODAL\_LOOPS\_PERMITTED is not defined or the callback parameter is nonnull, this function will return immediately. The object passed as the callback argument will receive the result of the alert window asynchronously. Otherwise, if JUCE\_MODAL\_LOOPS\_PERMITTED is defined and the callback parameter is null, the box is shown modally, and the method will block until the user has clicked the button (or pressed the escape or return keys). This mode of operation can cause problems, especially in plugins, so it is not recommended.Parameters

 iconType the type of icon to show 
 
 title the headline to show at the top of the box 
 message a longer, more descriptive message to show underneath the headline 
 button1Text the text to show in the first button if an empty string, then "yes" will be used (or a localised version of it) 
 button2Text the text to show in the first button if an empty string, then "no" will be used (or a localised version of it) 
 button3Text the text to show in the first button if an empty string, then "cancel" will be used (or a localised version of it) 
 associatedComponent if this is nonnull, it specifies the component that the alert window should be associated with. Depending on the look and feel, this might be used for positioning of the alert window. 
 callback if this is nonnull, the menu will be launched asynchronously, returning immediately, and the callback will receive a call to its modalStateFinished() when the box is dismissed, with its parameter being 1 if the "yes" button was pressed, 2 for the "no" button, or 0 if it was cancelled. The callback object will be owned and deleted by the system, so make sure that it works safely and doesn't keep any references to objects that might be deleted before it gets called. 



ReturnsIf the callback parameter has been set, this returns 0. Otherwise, it returns one of the following values:0 if the third button was pressed (normally used for 'cancel')1 if the first button was pressed (normally used for 'yes')2 if the middle button was pressed (normally used for 'no')