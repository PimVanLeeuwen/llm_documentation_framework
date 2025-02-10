#### getAllCommands()


 virtual void ApplicationCommandTarget::getAllCommands ( Array< CommandID > & commands ) pure virtual 
 

This must return a complete list of commands that this target can handle.Your target should add all the command IDs that it handles to the array that is passedin.Implemented in CodeEditorComponent, and JUCEApplication.