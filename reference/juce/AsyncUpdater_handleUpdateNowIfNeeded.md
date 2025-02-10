#### handleUpdateNowIfNeeded()


 void AsyncUpdater::handleUpdateNowIfNeeded ( ) 
 

If an update has been triggered and is pending, this will invoke it synchronously.Use this as a kind of "flush" operation if an update is pending, the handleAsyncUpdate() method will be called immediately; if no update is pending, then nothing will be done.Because this may invoke the callback, this method must only be called on the main event thread.