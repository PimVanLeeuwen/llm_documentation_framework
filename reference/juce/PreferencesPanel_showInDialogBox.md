#### showInDialogBox()


 void PreferencesPanel::showInDialogBox ( const String & dialogTitle, 
 
 int dialogWidth, 
 int dialogHeight, 
 Colour backgroundColour = Colours::white ) 

Utility method to display this panel in a DialogWindow.Calling this will create a DialogWindow containing this panel with the given size and title, and will run it modally, returning when the user closes the dialog box.