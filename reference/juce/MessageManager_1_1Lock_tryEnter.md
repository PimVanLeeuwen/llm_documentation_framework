#### tryEnter()


 bool MessageManager::Lock::tryEnter ( ) const noexcept 
 

Attempts to lock the message manager and exits if abort is called.This method behaves identically to enter, except that it will abort waiting for the lock if the abort method is called.Unlike other JUCE critical sections, this method will block waiting for the lock.To ensure predictable behaviour, you should recheck your abort condition if tryEnter returns false.This method can be used if you want to do some work while waiting for the MessageManagerLock:void doWorkWhileWaitingForMessageManagerLock() { MessageManager::Lock::ScopedTryLockType mmLock (messageManagerLock);while (! mmLock.isLocked()) { while (workQueue.size() > 0) { auto work = workQueue.pop(); doSomeWork (work); }this will block until we either have the lock or there is work mmLock.retryLock(); }we have the mmlock do some message manager stuff like resizing and painting components }called from another thread void addWorkToDo (Work work) { queue.push (work); messageManagerLock.abort(); }Returnsfalse if waiting for a lock was aborted, true if the lock was acquired. 
See alsoenter, abort, ScopedTryLock