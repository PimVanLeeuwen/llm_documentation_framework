#### quit()


 static void JUCEApplicationBase::quit ( ) static 
 

Signals that the main message loop should stop and the application should terminate.This isn't synchronous, it just posts a quit message to the main queue, and when this message arrives, the message loop will stop, the shutdown() method will be called, and the app will exit.Note that this will cause an unconditional quit to happen, so if you need an extra level before this, e.g. to give the user the chance to save their work and maybe cancel the quit, you'll need to handle this in the systemRequestedQuit() method see that method's help for more info.See alsoMessageManager Referenced by StandaloneFilterWindow::closeButtonPressed().