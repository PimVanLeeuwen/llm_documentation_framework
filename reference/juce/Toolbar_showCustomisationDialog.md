#### showCustomisationDialog()


 void Toolbar::showCustomisationDialog ( ToolbarItemFactory & factory, 
 
 int optionFlags = allCustomisationOptionsEnabled ) 

Pops up a modal dialog box that allows this toolbar to be customised by the user.The dialog contains a ToolbarItemPalette and various controls for editing other aspects of the toolbar. The dialog box will be opened modally, but the method will return immediately.The factory is used to determine the set of items that will be shown on the palette.The optionFlags parameter is a bitwiseor of values from the CustomisationFlags enum.See alsoToolbarItemPalette