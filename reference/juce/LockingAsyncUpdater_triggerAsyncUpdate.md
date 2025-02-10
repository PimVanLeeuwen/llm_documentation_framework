#### triggerAsyncUpdate()


 void LockingAsyncUpdater::triggerAsyncUpdate ( ) 
 

Causes the callback to be triggered at a later time.This method returns quickly, after which a callback to the handleAsyncUpdate() method will be made by the impl thread as soon as possible.If an update callback is already pending but hasn't started yet, calling this method will have no effect.It's threadsafe to call this method from any thread, BUT beware of calling it from a realtime (e.g. audio) thread, because it unconditionally locks a mutex. This may block, e.g. if this is called from a background thread while the async callback is in progress on the main thread.