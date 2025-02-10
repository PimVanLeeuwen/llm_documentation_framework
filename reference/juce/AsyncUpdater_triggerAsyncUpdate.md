#### triggerAsyncUpdate()


 void AsyncUpdater::triggerAsyncUpdate ( ) 
 

Causes the callback to be triggered at a later time.This method returns immediately, after which a callback to the handleAsyncUpdate() method will be made by the message thread as soon as possible.If an update callback is already pending but hasn't happened yet, calling this method will have no effect.It's threadsafe to call this method from any thread, BUT beware of calling it from a realtime (e.g. audio) thread, because it involves posting a message to the system queue, which means it may block (and in general will do on most OSes).