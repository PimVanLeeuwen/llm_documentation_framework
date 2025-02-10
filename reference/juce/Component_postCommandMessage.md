#### postCommandMessage()


 void Component::postCommandMessage ( int commandId ) 
 

Dispatches a numbered message to this component.This is a quick and cheap way of allowing simple asynchronous messages to be sent to components. It's also safe, because if the component that you send the message to is a null or dangling pointer, this won't cause an error.The command ID is later delivered to the component's handleCommandMessage() method by the application's message queue.See alsohandleCommandMessage