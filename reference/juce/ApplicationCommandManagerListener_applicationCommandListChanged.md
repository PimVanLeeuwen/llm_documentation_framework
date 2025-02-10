#### applicationCommandListChanged()


 virtual void ApplicationCommandManagerListener::applicationCommandListChanged ( ) pure virtual 
 

Called when commands are registered or deregistered from the command manager, or when commands are made active or inactive.Note that if you're using this to watch for changes to whether a command is disabled, you'll need to make sure that ApplicationCommandManager::commandStatusChanged() is called whenever the status of your command might have changed.Implemented in MenuBarModel.