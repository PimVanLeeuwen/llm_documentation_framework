template<class LockType>
class GenericScopedUnlock< LockType >Automatically unlocks and relocks a mutex object.This is the reverse of a GenericScopedLock object instead of locking the mutex for the lifetime of this object, it unlocks it.Make sure you don't try to unlock mutexes that aren't actually locked!e.g.CriticalSection myCriticalSection;
 
for (;;)
{
 const GenericScopedLock<CriticalSection> myScopedLock (myCriticalSection);
 // myCriticalSection is now locked
 
 ... do some stuff with it locked ..
 
 while (xyz)
 {
 ... do some stuff with it locked ..
 
 const GenericScopedUnlock<CriticalSection> unlocker (myCriticalSection);
 
 // myCriticalSection is now unlocked for the remainder of this block,
 // and relocked at the end.
 
 ...do some stuff with it unlocked ...
 }
 
 // myCriticalSection gets unlocked here.
}
CriticalSectionA reentrant mutex.Definition juce\_CriticalSection.h:58
GenericScopedLockAutomatically locks and unlocks a mutex object.Definition juce\_ScopedLock.h:70
GenericScopedUnlockAutomatically unlocks and relocks a mutex object.Definition juce\_ScopedLock.h:141
See alsoGenericScopedLock, CriticalSection, ScopedLock, ScopedUnlock 

Constructor & Destructor Documentation


◆ GenericScopedUnlock()


template<class LockType > 

 GenericScopedUnlock< LockType >::GenericScopedUnlock ( const LockType & lock ) explicitnoexcept 
 

Creates a GenericScopedUnlock.As soon as it is created, this will unlock the CriticalSection, and when the ScopedLock object is deleted, the CriticalSection will be relocked.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen! Best just to use it as a local stack object, rather than creating one with the new() operator.

◆ ~GenericScopedUnlock()


template<class LockType > 

 GenericScopedUnlock< LockType >::~GenericScopedUnlock ( ) noexcept 
 

Destructor.The CriticalSection will be unlocked when the destructor is called.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen!