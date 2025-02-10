#### handleCommandMessage()


 virtual void Component::handleCommandMessage ( int commandId ) virtual 
 

Called to handle a command that was sent by postCommandMessage().This is called by the message thread when a command message arrives, and the component can override this method to process it in any way it needs to.See alsopostCommandMessage Reimplemented in Button, CallOutBox, and MenuBarComponent.