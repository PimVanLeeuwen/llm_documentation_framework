#### initialise()


 virtual void JUCEApplicationBase::initialise ( const String & commandLineParameters ) pure virtual 
 

Called when the application starts.This will be called once to let the application do whatever initialisation it needs, create its windows, etc.After the method returns, the normal eventdispatch loop will be run, until the quit() method is called, at which point the shutdown() method will be called to let the application clear up anything it needs to delete.If during the initialise() method, the application decides not to startup after all, it can just call the quit() method and the event loop won't be run.Parameters

 commandLineParameters the line passed in does not include the name of the executable, just the parameter list. To get the parameters as an array, you can call JUCEApplication::getCommandLineParameters() 
 



See alsoshutdown, quit