#### sendChangeMessage()


 void Value::ValueSource::sendChangeMessage ( bool dispatchSynchronously ) 
 

Delivers a change message to all the listeners that are registered with this value.If dispatchSynchronously is true, the method will call all the listeners before returning; otherwise it'll dispatch a message and make the call later.

Member Data Documentation