#### showMessageBox()


 static void JUCE\_CALLTYPE AlertWindow::showMessageBox ( MessageBoxIconType iconType, const String & title, const String & message, const String & buttonText = String(), Component \* associatedComponent = nullptr ) static 
 

Shows a dialog box that just has a message and a single button to get rid of it.The box is shown modally, and the method will block until the user has clicked the button (or pressed the escape or return keys).Parameters

 iconType the type of icon to show 
 
 title the headline to show at the top of the box 
 message a longer, more descriptive message to show underneath the headline 
 buttonText the text to show in the button if this string is empty, the default string "OK" (or a localised version) will be used. 
 associatedComponent if this is nonnull, it specifies the component that the alert window should be associated with. Depending on the look and feel, this might be used for positioning of the alert window.