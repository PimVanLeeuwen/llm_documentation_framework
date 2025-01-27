#### cancelPendingUpdate()


 void AsyncUpdater::cancelPendingUpdate ( ) noexcept 
 

This will stop any pending updates from happening.If called after triggerAsyncUpdate() and before the handleAsyncUpdate() callback happens, this will cancel the handleAsyncUpdate() callback.Note that this method simply cancels the next callback if a callback is already in progress on a different thread, this won't block until the callback finishes, so there's no guarantee that the callback isn't still running when the method returns.