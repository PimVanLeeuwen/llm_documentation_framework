Automatically locks and unlocks a ReadWriteLock object.Use one of these as a local variable to control access to a ReadWriteLock.e.g.ReadWriteLock myLock;
 
for (;;)
{
 const ScopedReadLock myScopedLock (myLock);
 // myLock is now locked
 
 ...do some stuff...
 
 // myLock gets unlocked here.
}
ReadWriteLockA critical section that allows multiple simultaneous readers.Definition juce\_ReadWriteLock.h:63
ScopedReadLockAutomatically locks and unlocks a ReadWriteLock object.Definition juce\_ScopedReadLock.h:67
See alsoReadWriteLock, ScopedWriteLock 

Constructor & Destructor Documentation


◆ ScopedReadLock()


 ScopedReadLock::ScopedReadLock ( const ReadWriteLock & lock ) explicitnoexcept 
 

Creates a ScopedReadLock.As soon as it is created, this will call ReadWriteLock::enterRead(), and when the ScopedReadLock object is deleted, the ReadWriteLock will be unlocked.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen! Best just to use it as a local stack object, rather than creating one with the new() operator.

◆ ~ScopedReadLock()


 ScopedReadLock::~ScopedReadLock ( ) noexcept 
 

Destructor.The ReadWriteLock's exitRead() method will be called when the destructor is called.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen!