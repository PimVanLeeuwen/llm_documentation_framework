#### tryLock

```
boolean tryLock(long time,
                TimeUnit unit)
         throws InterruptedException
```
Acquires the lock if it is free within the given waiting time and the
current thread has not been interrupted.If the lock is available this method returns immediately
with the value `true`.
If the lock is not available then
the current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:The lock is acquired by the current thread; orSome other thread interrupts the
current thread, and interruption of lock acquisition is supported; orThe specified waiting time elapsesIf the lock is acquired then the value `true` is returned.If the current thread:has its interrupted status set on entry to this method; oris interrupted while acquiring
the lock, and interruption of lock acquisition is supported,then `InterruptedException` is thrown and the current thread's
interrupted status is cleared.If the specified waiting time elapses then the value `false`
is returned.
If the time is
less than or equal to zero, the method will not wait at all.Implementation ConsiderationsThe ability to interrupt a lock acquisition in some implementations
may not be possible, and if possible may
be an expensive operation.
The programmer should be aware that this may be the case. An
implementation should document when this is the case.An implementation can favor responding to an interrupt over normal
method return, or reporting a timeout.A `Lock` implementation may be able to detect
erroneous use of the lock, such as an invocation that would cause
deadlock, and may throw an (unchecked) exception in such circumstances.
The circumstances and the exception type must be documented by that
`Lock` implementation.
Parameters:
`time` - the maximum time to wait for the lock
`unit` - the time unit of the `time` argument
Returns:
`true` if the lock was acquired and `false`
if the waiting time elapsed before the lock was acquired
Throws:
`InterruptedException` - if the current thread is interrupted
while acquiring the lock (and interruption of lock
acquisition is supported)

