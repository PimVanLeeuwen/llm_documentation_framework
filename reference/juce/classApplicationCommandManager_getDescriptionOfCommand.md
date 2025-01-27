#### getDescriptionOfCommand()


 String ApplicationCommandManager::getDescriptionOfCommand ( CommandID commandID ) const noexcept 
 

Returns the description field for a command.An empty string is returned if no command with this ID has been registered. If the command has no description, this will return its short name field instead.See alsogetNameOfCommand