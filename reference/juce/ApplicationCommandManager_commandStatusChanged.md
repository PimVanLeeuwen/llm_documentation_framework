#### commandStatusChanged()


 void ApplicationCommandManager::commandStatusChanged ( ) 
 

This should be called to tell the manager that one of its registered commands may have changed its active status.Because the command manager only finds out whether a command is active or inactive by querying the current ApplicationCommandTarget, this is used to tell it that things may have changed. It allows things like buttons to update their enablement, etc.This method will cause an asynchronous call to ApplicationCommandManagerListener::applicationCommandListChanged() for any registered listeners.