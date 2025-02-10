#### makeOptionsYesNoCancel()


 static MessageBoxOptions MessageBoxOptions::makeOptionsYesNoCancel ( MessageBoxIconType iconType, const String & title, const String & message, const String & button1Text = String(), const String & button2Text = String(), const String & button3Text = String(), Component \* associatedComponent = nullptr ) static 
 

Creates options suitable for a message box with three buttons.If no button text is supplied, "Yes", "No", and "Cancel" will be used.