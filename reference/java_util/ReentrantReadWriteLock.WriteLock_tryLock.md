#### tryLock

```
public boolean tryLock(long timeout,
                       TimeUnit unit)
                throws InterruptedException
```
Acquires the write lock if it is not held by another thread
within the given waiting time and the current thread has
not been interrupted.Acquires the write lock if neither the read nor write lock
are held by another thread
and returns immediately with the value `true`,
setting the write lock hold count to one. If this lock has been
set to use a fair ordering policy then an available lock
will not be acquired if any other threads are
waiting for the write lock. This is in contrast to the `tryLock()` method. If you want a timed `tryLock`
that does permit barging on a fair lock then combine the
timed and un-timed forms together:
```
 
 if (lock.tryLock() ||
     lock.tryLock(timeout, unit)) {
   ...
 }
```
If the current thread already holds this lock then the
hold count is incremented by one and the method returns
`true`.If the lock is held by another thread then the current
thread becomes disabled for thread scheduling purposes and
lies dormant until one of three things happens:The write lock is acquired by the current thread; orSome other thread interrupts
the current thread; orThe specified waiting time elapsesIf the write lock is acquired then the value `true` is
returned and the write lock hold count is set to one.If the current thread:has its interrupted status set on entry to this method;
oris interrupted while
acquiring the write lock,then `InterruptedException` is thrown and the current
thread's interrupted status is cleared.If the specified waiting time elapses then the value
`false` is returned. If the time is less than or
equal to zero, the method will not wait at all.In this implementation, as this method is an explicit
interruption point, preference is given to responding to
the interrupt over normal or reentrant acquisition of the
lock, and over reporting the elapse of the waiting time.
Specified by:
`tryLock` in interface `Lock`
Parameters:
`timeout` - the time to wait for the write lock
`unit` - the time unit of the timeout argument
Returns:
`true` if the lock was free and was acquired
by the current thread, or the write lock was already held by the
current thread; and `false` if the waiting time
elapsed before the lock could be acquired.
Throws:
`InterruptedException` - if the current thread is interrupted
`NullPointerException` - if the time unit is null

