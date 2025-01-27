#### readLockInterruptibly

```
public long readLockInterruptibly()
                           throws InterruptedException
```
Non-exclusively acquires the lock, blocking if necessary
until available or the current thread is interrupted.
Behavior under interruption matches that specified
for method `Lock.lockInterruptibly()`.
Returns:
a stamp that can be used to unlock or convert mode
Throws:
`InterruptedException` - if the current thread is interrupted
before acquiring the lock

