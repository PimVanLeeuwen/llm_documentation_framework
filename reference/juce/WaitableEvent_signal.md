#### signal()


 void WaitableEvent::signal ( ) const 
 

Wakes up any threads that are currently waiting on this object.If signal() is called when nothing is waiting, the next thread to call wait() will return immediately and reset the signal.If the WaitableEvent is manual reset, all current and future threads that wait upon this object will be woken, until reset() is explicitly called.If the WaitableEvent is automatic reset, and one or more threads is waiting upon the object, then one of them will be woken up. If no threads are currently waiting, then the next thread to call wait() will be woken up. As soon as a thread is woken, the signal is automatically reset.See alsowait, reset