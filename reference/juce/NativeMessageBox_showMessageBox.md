#### showMessageBox()


 static void JUCE\_CALLTYPE NativeMessageBox::showMessageBox ( MessageBoxIconType iconType, const String & title, const String & message, Component \* associatedComponent = nullptr ) static 
 

Shows a dialog box that just has a message and a single 'ok' button to close it.The box is shown modally, and the method will block until the user has clicked its button (or pressed the escape or return keys).Parameters

 iconType the type of icon to show. 
 
 title the headline to show at the top of the box. 
 message a longer, more descriptive message to show underneath the title. 
 associatedComponent if this is nonnull, it specifies the component that the alert window should be associated with. Depending on the look and feel, this might be used for positioning of the alert window.