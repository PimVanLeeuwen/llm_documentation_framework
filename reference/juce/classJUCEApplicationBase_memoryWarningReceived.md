#### memoryWarningReceived()


 virtual void JUCEApplicationBase::memoryWarningReceived ( ) virtual 
 

Called by the operating system to indicate that you should reduce your memory footprint.You should override this method to free up some memory gracefully, if possible, otherwise the host may forcibly kill your app.At the moment this method is only called on iOS.References jassertfalse.