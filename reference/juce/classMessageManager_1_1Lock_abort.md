#### abort()


 void MessageManager::Lock::abort ( ) const noexcept 
 

Unblocks a thread which is waiting in tryEnter Call this method if you want to unblock a thread which is waiting for the MessageManager lock in tryEnter.This method does not have any effect on a thread waiting for a lock in enter.See alsotryEnter