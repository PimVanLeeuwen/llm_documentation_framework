#### moreThanOneInstanceAllowed()


 bool JUCEApplication::moreThanOneInstanceAllowed ( ) overridevirtual 
 

Checks whether multiple instances of the app are allowed.If your application class returns true for this, more than one instance is permitted to run (except on OSX where the OS automatically stops you launching a second instance of an app without explicitly starting it from the commandline).If it's false, the second instance won't start, but you will still get a callback to anotherInstanceStarted() to tell you about this which gives you a chance to react to what the user was trying to do.Implements JUCEApplicationBase.