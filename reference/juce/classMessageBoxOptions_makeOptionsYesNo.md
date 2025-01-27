#### makeOptionsYesNo()


 static MessageBoxOptions MessageBoxOptions::makeOptionsYesNo ( MessageBoxIconType iconType, const String & title, const String & message, const String & button1Text = String(), const String & button2Text = String(), Component \* associatedComponent = nullptr ) static 
 

Creates options suitable for a message box with two buttons.If no button text is supplied, "Yes" and "No" will be used.