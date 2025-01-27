#### registerAllCommandsForTarget()


 void ApplicationCommandManager::registerAllCommandsForTarget ( ApplicationCommandTarget \* target ) 
 

Adds all the commands that this target publishes to the manager's list.This will use ApplicationCommandTarget::getAllCommands() and ApplicationCommandTarget::getCommandInfo() to get details about all the commands that this target can do, and will call registerCommand() to add each one to the manger's list.See alsoregisterCommand