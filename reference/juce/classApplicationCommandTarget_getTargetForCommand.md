#### getTargetForCommand()


 ApplicationCommandTarget \* ApplicationCommandTarget::getTargetForCommand ( CommandID commandID ) 
 

Searches this target and all subsequent ones for the first one that can handle the specified command.This will use getNextCommandTarget() to determine the chain of targets to try after this one.