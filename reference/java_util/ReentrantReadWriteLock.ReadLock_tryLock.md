#### tryLock

```
public boolean tryLock(long timeout,
                       TimeUnit unit)
                throws InterruptedException
```
Acquires the read lock if the write lock is not held by
another thread within the given waiting time and the
current thread has not been interrupted.Acquires the read lock if the write lock is not held by
another thread and returns immediately with the value
`true`. If this lock has been set to use a fair
ordering policy then an available lock will not be
acquired if any other threads are waiting for the
lock. This is in contrast to the `tryLock()`
method. If you want a timed `tryLock` that does
permit barging on a fair lock then combine the timed and
un-timed forms together:
```
 
 if (lock.tryLock() ||
     lock.tryLock(timeout, unit)) {
   ...
 }
```
If the write lock is held by another thread then the
current thread becomes disabled for thread scheduling
purposes and lies dormant until one of three things happens:The read lock is acquired by the current thread; orSome other thread interrupts
the current thread; orThe specified waiting time elapses.If the read lock is acquired then the value `true` is
returned.If the current thread:has its interrupted status set on entry to this method; oris interrupted while
acquiring the read lock,then `InterruptedException` is thrown and the
current thread's interrupted status is cleared.If the specified waiting time elapses then the value
`false` is returned. If the time is less than or
equal to zero, the method will not wait at all.In this implementation, as this method is an explicit
interruption point, preference is given to responding to
the interrupt over normal or reentrant acquisition of the
lock, and over reporting the elapse of the waiting time.
Specified by:
`tryLock` in interface `Lock`
Parameters:
`timeout` - the time to wait for the read lock
`unit` - the time unit of the timeout argument
Returns:
`true` if the read lock was acquired
Throws:
`InterruptedException` - if the current thread is interrupted
`NullPointerException` - if the time unit is null

