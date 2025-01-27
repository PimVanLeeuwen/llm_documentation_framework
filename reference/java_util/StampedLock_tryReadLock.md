#### tryReadLock

```
public long tryReadLock(long time,
                        TimeUnit unit)
                 throws InterruptedException
```
Non-exclusively acquires the lock if it is available within the
given time and the current thread has not been interrupted.
Behavior under timeout and interruption matches that specified
for method `Lock.tryLock(long,TimeUnit)`.
Parameters:
`time` - the maximum time to wait for the lock
`unit` - the time unit of the `time` argument
Returns:
a stamp that can be used to unlock or convert mode,
or zero if the lock is not available
Throws:
`InterruptedException` - if the current thread is interrupted
before acquiring the lock

