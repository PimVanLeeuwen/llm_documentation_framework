#### enter()


 void MessageManager::Lock::enter ( ) const noexcept 
 

Acquires the message manager lock.If the caller thread already has exclusive access to the MessageManager, this method will return immediately. If another thread is currently using the MessageManager, this will wait until that thread releases the lock to the MessageManager.This call will only exit if the lock was acquired by this thread. Calling abort while a thread is waiting for enter to finish, will have no effect.See alsoexit, abort