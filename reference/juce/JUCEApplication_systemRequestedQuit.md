#### systemRequestedQuit()


 void JUCEApplication::systemRequestedQuit ( ) overridevirtual 
 

Called when the operating system is trying to close the application.The default implementation of this method is to call quit(), but it may be overloaded to ignore the request or do some other special behaviour instead. For example, you might want to offer the user the chance to save their changes before quitting, and give them the chance to cancel.If you want to send a quit signal to your app, this is the correct method to call, because it means that requests that come from the system get handled in the same way as those from your own application code. So e.g. you'd call this method from a "quit" item on a menu bar.Implements JUCEApplicationBase.