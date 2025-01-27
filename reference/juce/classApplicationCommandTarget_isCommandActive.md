#### isCommandActive()


 bool ApplicationCommandTarget::isCommandActive ( CommandID commandID ) 
 

Checks whether this command can currently be performed by this target.This will return true only if a call to getCommandInfo() doesn't set the isDisabled flag to indicate that the command is inactive.