#### getCommandForID()


 const ApplicationCommandInfo \* ApplicationCommandManager::getCommandForID ( CommandID commandID ) const noexcept 
 

Returns the details about a given command ID.This will search the list of registered commands for one with the given command ID number, and return its associated info. If no matching command is found, this will return nullptr.