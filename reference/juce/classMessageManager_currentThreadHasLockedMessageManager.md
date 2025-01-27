#### currentThreadHasLockedMessageManager()


 bool MessageManager::currentThreadHasLockedMessageManager ( ) const noexcept 
 

Returns true if the caller thread has currently got the message manager locked.see the MessageManagerLock class for more info about this.This will be true if the caller is the message thread, because that automatically gains a lock while a message is being dispatched.