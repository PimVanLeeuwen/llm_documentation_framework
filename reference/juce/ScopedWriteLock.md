Automatically locks and unlocks a ReadWriteLock object.Use one of these as a local variable to control access to a ReadWriteLock.e.g.ReadWriteLock myLock;
 
for (;;)
{
 const ScopedWriteLock myScopedLock (myLock);
 // myLock is now locked
 
 ...do some stuff...
 
 // myLock gets unlocked here.
}
ReadWriteLockA critical section that allows multiple simultaneous readers.Definition juce\_ReadWriteLock.h:63
ScopedWriteLockAutomatically locks and unlocks a ReadWriteLock object.Definition juce\_ScopedWriteLock.h:67
See alsoReadWriteLock, ScopedReadLock 

Constructor & Destructor Documentation


◆ ScopedWriteLock()


 ScopedWriteLock::ScopedWriteLock ( const ReadWriteLock & lock ) explicitnoexcept 
 

Creates a ScopedWriteLock.As soon as it is created, this will call ReadWriteLock::enterWrite(), and when the ScopedWriteLock object is deleted, the ReadWriteLock will be unlocked.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen! Best just to use it as a local stack object, rather than creating one with the new() operator.

◆ ~ScopedWriteLock()


 ScopedWriteLock::~ScopedWriteLock ( ) noexcept 
 

Destructor.The ReadWriteLock's exitWrite() method will be called when the destructor is called.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen!