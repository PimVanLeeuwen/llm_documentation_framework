template<class LockType>
class GenericScopedLock< LockType >Automatically locks and unlocks a mutex object.Use one of these as a local variable to provide RAIIbased locking of a mutex.The templated class could be a CriticalSection, SpinLock, or anything else that provides enter() and exit() methods.e.g.CriticalSection myCriticalSection;
 
for (;;)
{
 const GenericScopedLock<CriticalSection> myScopedLock (myCriticalSection);
 // myCriticalSection is now locked
 
 ...do some stuff...
 
 // myCriticalSection gets unlocked here.
}
CriticalSectionA reentrant mutex.Definition juce\_CriticalSection.h:58
GenericScopedLockAutomatically locks and unlocks a mutex object.Definition juce\_ScopedLock.h:70
See alsoGenericScopedUnlock, CriticalSection, SpinLock, ScopedLock, ScopedUnlock 

Constructor & Destructor Documentation


◆ GenericScopedLock()


template<class LockType > 

 GenericScopedLock< LockType >::GenericScopedLock ( const LockType & lock ) explicitnoexcept 
 

Creates a GenericScopedLock.As soon as it is created, this will acquire the lock, and when the GenericScopedLock object is deleted, the lock will be released.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen! Best just to use it as a local stack object, rather than creating one with the new() operator.

◆ ~GenericScopedLock()


template<class LockType > 

 GenericScopedLock< LockType >::~GenericScopedLock ( ) noexcept 
 

Destructor.The lock will be released when the destructor is called. Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen!