#### userTriedToCloseWindow()


 virtual void Component::userTriedToCloseWindow ( ) virtual 
 

For components on the desktop, this is called if the system wants to close the window.This is a signal that either the user or the system wants the window to close. The default implementation of this method will trigger an assertion to warn you that your component should do something about it, but you can override this to ignore the event if you want.Reimplemented in AlertWindow.