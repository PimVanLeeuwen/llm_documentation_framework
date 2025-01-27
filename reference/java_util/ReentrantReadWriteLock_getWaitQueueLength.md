#### getWaitQueueLength

```
public int getWaitQueueLength(Condition condition)
```
Returns an estimate of the number of threads waiting on the
given condition associated with the write lock. Note that because
timeouts and interrupts may occur at any time, the estimate
serves only as an upper bound on the actual number of waiters.
This method is designed for use in monitoring of the system
state, not for synchronization control.
Parameters:
`condition` - the condition
Returns:
the estimated number of waiting threads
Throws:
`IllegalMonitorStateException` - if this lock is not held
`IllegalArgumentException` - if the given condition is
not associated with this lock
`NullPointerException` - if the condition is null

