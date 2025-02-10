#### cancelPendingUpdate()


 void LockingAsyncUpdater::cancelPendingUpdate ( ) noexcept 
 

This will stop any pending updates from happening.If a callback is already in progress on another thread, this will block until the callback has finished before returning.