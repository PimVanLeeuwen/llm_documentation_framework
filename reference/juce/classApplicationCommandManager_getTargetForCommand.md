#### getTargetForCommand()


 ApplicationCommandTarget \* ApplicationCommandManager::getTargetForCommand ( CommandID commandID, 
 
 ApplicationCommandInfo & upToDateInfo ) 

Tries to find the best target to use to perform a given command.This will call getFirstCommandTarget() to find the preferred target, and will check whether that target can handle the given command. If it can't, then it'll use ApplicationCommandTarget::getNextCommandTarget() to find the next one to try, and so on until no more are available.If no targets are found that can perform the command, this method will return nullptr.If a target is found, then it will get the target to fillin the upToDateInfo structure with the latest info about that command, so that the caller can see whether the command is disabled, ticked, etc.