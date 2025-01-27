#### setCommandToTrigger()


 void Button::setCommandToTrigger ( ApplicationCommandManager \* commandManagerToUse, 
 
 CommandID commandID, 
 bool generateTooltip ) 

Sets a command ID for this button to automatically invoke when it's clicked.When the button is pressed, it will use the given manager to trigger the command ID.Obviously be careful that the ApplicationCommandManager doesn't get deleted before this button is. To disable the command triggering, call this method and pass nullptr as the command manager.If generateTooltip is true, then the button's tooltip will be automatically generated based on the name of this command and its current shortcut key.See alsoaddShortcut, getCommandID